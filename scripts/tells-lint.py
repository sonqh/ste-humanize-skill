#!/usr/bin/env python3
"""Deterministic linter for the AI-writing tells in SKILL.md.

Checks only patterns a regex can see. It never judges meaning, never flags
hedges, and never checks whether a rewrite kept the original claim.

Usage:
    tells-lint.py FILE [FILE ...]
    echo "text" | tells-lint.py [--json]
    tells-lint.py --baseline 5 FILE       # pass unless hard findings exceed 5
    tells-lint.py --disable dash,stock-word FILE
    tells-lint.py --selftest

Exit 1 when hard findings exceed the baseline (default 0).
Advisory findings never fail the run.
Exit 2 on a usage error.
"""
import argparse
import json
import re
import sys

STOCK_WORDS = [
    "additionally", "align with", "bolster", "crucial", "deep dive", "delve",
    "enduring", "enhance", "garner", "interplay", "intricate", "intricacies",
    "leverage", "meticulous", "meticulously", "pivotal", "seamless", "seamlessly",
    "showcase", "tapestry", "testament", "underscore", "underscores", "vibrant",
    "game-changer", "game changer", "cutting-edge", "cutting edge",
]

# REQ-TELLS-001: stock words that take verb or noun inflections.
STOCK_VERBS = {"align with", "bolster", "delve", "enhance", "garner", "leverage",
               "showcase", "underscore"}
STOCK_NOUNS = {"deep dive", "game-changer", "game changer", "interplay",
               "tapestry", "testament"}


def stock_pattern(word):
    """Return a regex for one stock word with its inflections."""
    if word in STOCK_VERBS:
        head, sep, tail = word.partition(" ")
        if head.endswith("e"):
            core = re.escape(head[:-1]) + r"(?:e|es|ed|ing)"
        else:
            core = re.escape(head) + r"(?:s|es|ed|ing)?"
        return core + (r"\s+" + re.escape(tail) if sep else "")
    if word in STOCK_NOUNS:
        if word.endswith("y"):
            return re.escape(word[:-1]) + r"(?:y|ies)"
        return re.escape(word) + r"(?:s|es)?"
    return re.escape(word)


SALES_WORDS = [
    "nestled", "breathtaking", "renowned", "must-visit", "stunning",
    "diverse array", "in the heart of", "profound",
]

CHAT_RESIDUE = [
    r"great question", r"i hope this helps", r"\bof course!", r"\bcertainly!",
    r"you're absolutely right", r"would you like me to", r"want me to",
    r"let me know if", r"should i continue",
]

RUN_UP = [
    r"let'?s dive in", r"let'?s explore", r"let'?s break this down",
    r"here'?s what you need to know", r"without further ado", r"here'?s the thing",
    r"the thing is,", r"real talk", r"let'?s be honest",
]

DEEP_SAYINGS = [
    r"\bat its core\b", r"\bthe real question is\b", r"\bwhat really matters\b",
    r"\bthe heart of the matter\b", r"\bis the (?:language|currency|architecture) of\b",
]


# REQ-TELLS-004: tells of decision pages.
FALSE_BALANCE = [
    r"\b(?:both|all) (?:options|approaches|choices) have (?:their )?(?:own )?(?:merits|pros and cons|strengths|trade-?offs)",
    r"\beach (?:option|approach|choice) has (?:its )?(?:own )?(?:merits|pros and cons|strengths|trade-?offs)",
    r"\bit (?:all )?depends on (?:your|our|the team'?s|the) (?:needs|use case|requirements|context)",
    r"\bthere is no one-size-fits-all", r"\bno silver bullet",
    r"\bthe (?:right|best) (?:choice|option|approach) depends on",
]

ACTORLESS_DECISION = [
    r"\bit (?:was|has been|is) decided\b", r"\ba decision (?:was|has been) (?:made|taken)\b",
    r"\bit is (?:recommended|proposed|suggested|advised) (?:that|to)\b",
]

EMPTY_MITIGATION = [
    r"\bmonitor(?:ed|ing|s)? (?:closely|carefully)\b", r"\bclosely monitor(?:ed|ing|s)?\b",
    r"\bcareful(?:ly)? (?:planning|plan|consider\w*|evaluat\w*)\b", r"\bensure proper\b",
    r"\bthorough(?:ly)? test\w*", r"\bfollow(?:s|ing)? best practices\b",
]

QUALITY_WORDS = [
    "scalable", "scalability", "performant", "future-proof", "flexible", "maintainable",
    "reliable", "efficient", "battle-tested", "enterprise-grade", "production-ready", "best-in-class",
]

# REQ-TELLS-005: tells of messages to users and customers, in English and Vietnamese.
SUPPORT_CLICHE = [
    r"\bunfortunately\b", r"\bplease note\b", r"\b(?:we )?apologi[sz]e for any inconvenience",
    r"\bsorry for (?:any|the) inconvenience", r"\brest assured\b",
    r"\bwe value your (?:feedback|business)\b", r"\bwe understand your frustration\b",
    r"\b(?:don'?t|do not) hesitate to\b", r"\bfeel free to (?:contact|reach)\b",
    r"(?:sự )?bất tiện này", r"\bxin lỗi vì sự bất tiện",
    r"\bmong (?:anh/chị|quý khách|anh|chị|bạn) (?:thông cảm|thông cảm cho)",
    r"\bhy vọng thông tin (?:trên|này) (?:hữu ích|có ích)", r"\b(?:đừng|không) ngần ngại\b",
    r"\bluôn lắng nghe\b", r"\btrân trọng ý kiến\b",
]

VAGUE_DATE = [
    r"\bsoon\b", r"\bshortly\b", r"\bin the coming days\b", r"\bas soon as possible\b", r"\basap\b",
    r"thời gian sớm nhất", r"\bsớm nhất có thể\b", r"\btrong (?:vài|mấy|những) ngày tới\b", r"\bsắp tới\b",
]

BLAME_PHRASE = [
    r"\byou (?:failed|forgot|neglected) to\b", r"\byou should have\b", r"\bdue to your (?:error|mistake)\b",
    r"\b(?:anh|chị|bạn|quý khách) (?:đã )?(?:quên|nhập sai)\b",
]

NEGATIVE_CONTRACTION = (r"\b(?:can|don|won|isn|aren|wasn|weren|doesn|didn|shouldn|wouldn|couldn"
                        r"|haven|hasn|hadn|mustn)['’]t\b")

# REQ-TELLS-005: "dạ" and "ạ" as whole words.
PARTICLE = re.compile(r"(?<!\w)d?ạ(?!\w)", re.I)

# REQ-TELLS-001: the Vietnamese form of not-x-but-y.
NOT_X_BUT_Y_VI = r"\bkhông phải\b[^.?!;:]{1,60}?\bmà\b"

# REQ-TELLS-001 REQ-TELLS-002
RULES = {
    # hard rules
    "dash": ("hard", re.compile(r"—|–|(?<=\S) -- (?=\S)|\s--\s")),
    "not-x-but-y": ("hard", re.compile(
        r"\b(?:not|isn'?t|aren'?t|wasn'?t|it'?s not)\s+(?:just|only|merely|simply|about)?\s*[^.?!;:]{1,60}?[,;]?\s+but\s+(?:rather\s+)?(?:also\s+)?|" + NOT_X_BUT_Y_VI, re.I)),
    "not-x-its-y": ("hard", re.compile(r"\b(?:it'?s|this is|that'?s) not [^.?!]{1,60}?(?:[,.:;]|\s-(?=\s)|\s*[—–])\s*(?:it'?s|it is|this is|that'?s)\b", re.I)),
    "chat-residue": ("hard", re.compile("|".join(CHAT_RESIDUE), re.I)),
    "run-up": ("hard", re.compile("|".join(RUN_UP), re.I)),
    "deep-saying": ("hard", re.compile("|".join(DEEP_SAYINGS), re.I)),
    "stock-word": ("hard", re.compile(r"\b(?:" + "|".join(stock_pattern(w) for w in STOCK_WORDS) + r")\b", re.I)),
    "bold-label": ("hard", re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\*\*[^*\n]+?(?::\*\*|\*\*\s*:)", re.M)),
    "emoji-heading": ("hard", re.compile(r"^#{1,6}\s*[\U0001F300-\U0001FAFF☀-➿]", re.M)),
    # advisory rules
    "sales-word": ("advisory", re.compile(r"\b(?:" + "|".join(re.escape(w) for w in SALES_WORDS) + r")\b", re.I)),
    "title-case-heading": ("advisory", re.compile(r"^#{1,6}\s+(?:[A-Z][a-z]+\s+){2,}[A-Z][a-z]+\s*$", re.M)),
    "stacked-qualifier": ("advisory", re.compile(r"\b(?:could|might|may)\s+(?:potentially|possibly|arguably)\s+(?:potentially|possibly|arguably|be)\b", re.I)),
    "serves-as": ("advisory", re.compile(r"\b(?:serves as|stands as|functions as|boasts|represents a)\b", re.I)),
    "closer": ("advisory", re.compile(r"^(?:That is the real win|That distinction matters|Read that again|Let that sink in)\.?\s*$", re.M | re.I)),
    "repeated-closer": ("advisory", None),
    # REQ-TELLS-004 advisory rules for decision pages
    "false-balance": ("advisory", re.compile("|".join(FALSE_BALANCE), re.I)),
    "actorless-decision": ("advisory", re.compile("|".join(ACTORLESS_DECISION), re.I)),
    "empty-mitigation": ("advisory", re.compile("|".join(EMPTY_MITIGATION), re.I)),
    "unmeasured-quality": ("advisory", re.compile(r"\b(?:" + "|".join(re.escape(w) for w in QUALITY_WORDS) + r")\b", re.I)),
    # REQ-TELLS-005 advisory rules for messages
    "support-cliche": ("advisory", re.compile("|".join(SUPPORT_CLICHE), re.I)),
    "vague-date": ("advisory", re.compile("|".join(VAGUE_DATE), re.I)),
    "blame-phrase": ("advisory", re.compile("|".join(BLAME_PHRASE), re.I)),
    "negative-contraction": ("advisory", re.compile(NEGATIVE_CONTRACTION, re.I)),
    "particle-repeat": ("advisory", None),
}

SENTENCE_END = re.compile(r"[.?!\n]")


def _sentence_has_digit(text, start, end):
    """REQ-TELLS-004: True when the sentence around text[start:end] holds a digit."""
    left = max(text.rfind(c, 0, start) for c in ".?!\n")
    m = SENTENCE_END.search(text, end)
    right = m.start() if m else len(text)
    return bool(re.search(r"\d", text[left + 1:right]))

FENCE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE = re.compile(r"`[^`\n]*`")
URL = re.compile(r"https?://\S+|\S+/\S+")


def strip_code(text):
    out, fenced = [], False
    for line in text.splitlines():
        if FENCE.match(line):
            fenced = not fenced
            out.append("")
            continue
        if fenced:
            out.append("")
            continue
        line = INLINE_CODE.sub(" ", line)
        line = URL.sub(" ", line)
        out.append(line)
    return "\n".join(out)


def line_of(text, pos):
    return text.count("\n", 0, pos) + 1


def lint(text, disabled=()):
    clean = strip_code(text)
    findings = []
    for name, (level, rx) in RULES.items():
        if name in disabled or rx is None:
            continue
        for m in rx.finditer(clean):
            if name == "unmeasured-quality" and _sentence_has_digit(clean, m.start(), m.end()):
                continue
            findings.append({
                "rule": name, "level": level,
                "line": line_of(clean, m.start()),
                "match": m.group(0).strip()[:80],
            })
    if "repeated-closer" not in disabled:
        paras = [p.strip() for p in re.split(r"\n\s*\n", clean) if p.strip()]
        one_liners = [p for p in paras if len(p) < 60 and "\n" not in p and not p.startswith("#")]
        seen = {}
        for p in one_liners:
            seen[p] = seen.get(p, 0) + 1
        for p, n in seen.items():
            if n >= 2:
                findings.append({"rule": "repeated-closer", "level": "advisory",
                                 "line": line_of(clean, clean.find(p)), "match": p})
    # REQ-TELLS-005 one finding per file, at the second "dạ" or "ạ"
    if "particle-repeat" not in disabled:
        particles = list(PARTICLE.finditer(clean))
        if len(particles) > 1:
            findings.append({"rule": "particle-repeat", "level": "advisory",
                             "line": line_of(clean, particles[1].start()),
                             "match": clean[max(clean.rfind("\n", 0, particles[1].start()) + 1,
                                                particles[1].start() - 20):particles[1].end()].strip()})
    findings.sort(key=lambda f: (f["line"], f["rule"]))
    return findings


def selftest():
    bad = ("It's not just a tool, it's a mirror. The policy — announced today — applies. "
           "Great question! Let's dive in. At its core it is robust and seamless.\n"
           "- **Speed:** fast\n")
    good = "The request may have failed. Check the client version. The tool shows your habits."
    f_bad = {f["rule"] for f in lint(bad)}
    f_good = lint(good)
    want = {"not-x-its-y", "dash", "chat-residue", "run-up", "deep-saying", "stock-word", "bold-label"}
    missing = want - f_bad
    assert not missing, f"selftest: missing {missing}"
    assert not f_good, f"selftest: false positive on hedge text: {f_good}"
    for text, rule in [
        ("It's not a tool: it's a mirror.", "not-x-its-y"),
        ("It's not a tool; it is a mirror.", "not-x-its-y"),
        ("It's not just a linter — it's a gate.", "not-x-its-y"),
        ("It's not just a linter - it's a gate.", "not-x-its-y"),
        ("The team leverages the cache and leveraged it, leveraging more.", "stock-word"),
        ("Two deep dives and a tapestry of testaments.", "stock-word"),
        ("Both options have their merits.", "false-balance"),
        ("It was decided that the team uses pg-boss.", "actorless-decision"),
        ("Mitigation: we will monitor closely.", "empty-mitigation"),
        ("Option B is more scalable.", "unmeasured-quality"),
        ("Không phải lỗi hệ thống mà là do cấu hình.", "not-x-but-y"),
        ("We apologize for any inconvenience.", "support-cliche"),
        ("Mong quý khách thông cảm.", "support-cliche"),
        ("We will fix it soon.", "vague-date"),
        ("Bên em sẽ xử lý trong thời gian sớm nhất.", "vague-date"),
        ("You forgot to save the file.", "blame-phrase"),
        ("We can't restore it.", "negative-contraction"),
        ("Dạ, em gửi anh ạ.", "particle-repeat"),
    ]:
        assert rule in {f["rule"] for f in lint(text)}, f"selftest: {rule} missed {text!r}"
    for text, rule in [
        ("It's not here. The tool works.", "not-x-its-y"),
        ("It's not a well-known fact, so we check.", "not-x-its-y"),
        ("Use a lever to lift the load.", "stock-word"),
        ("Option A is cheaper, so we choose it.", "false-balance"),
        ("The team decided to use pg-boss.", "actorless-decision"),
        ("Mitigation: run the load test on staging before the release.", "empty-mitigation"),
        ("Option B scales to 350 jobs per second.", "unmeasured-quality"),
        ("The queue was reliable for 30 days.", "unmeasured-quality"),
        ("Lỗi không phải do hệ thống.", "not-x-but-y"),
        ("We refunded the extra $29 today.", "support-cliche"),
        ("We will fix it on 3 March.", "vague-date"),
        ("The file was larger than 10 MB.", "blame-phrase"),
        ("We cannot restore it, and you'll get a refund.", "negative-contraction"),
        ("Dạ, em gửi anh bảng giá.", "particle-repeat"),
    ]:
        assert rule not in {f["rule"] for f in lint(text)}, f"selftest: {rule} false positive on {text!r}"
    print("selftest ok")


# REQ-TELLS-003
def main(argv):
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("files", nargs="*", help="Files to check. Read stdin if none.")
    ap.add_argument("--json", action="store_true", help="Print the findings as JSON.")
    ap.add_argument("--baseline", type=int, default=0, metavar="N",
                    help="Allow N hard findings. Default 0.")
    ap.add_argument("--disable", default="", metavar="RULES",
                    help="Turn off rules. Give names with commas.")
    ap.add_argument("--selftest", action="store_true", help="Run the built-in checks and exit.")
    a = ap.parse_args(argv)
    if a.selftest:
        selftest()
        return 0
    disabled = {d.strip() for d in a.disable.split(",") if d.strip()}
    unknown = disabled - set(RULES)
    if unknown:
        print(f"unknown rule(s): {', '.join(sorted(unknown))}", file=sys.stderr)
        return 2
    sources = []
    if a.files:
        for p in a.files:
            try:
                with open(p, encoding="utf-8") as fh:
                    sources.append((p, fh.read()))
            except OSError as e:
                print(f"cannot read {p}: {e}", file=sys.stderr)
                return 2
    else:
        data = sys.stdin.read()
        if not data.strip():
            print("no input", file=sys.stderr)
            return 2
        sources.append(("<stdin>", data))
    hard = 0
    report = []
    for name, text in sources:
        fs = lint(text, disabled)
        hard += sum(1 for f in fs if f["level"] == "hard")
        report.append({"file": name, "findings": fs})
        if not a.json:
            for f in fs:
                print(f"{name}:{f['line']}: [{f['level']}] {f['rule']}: {f['match']}")
    if a.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"{hard} hard finding(s), baseline {a.baseline}")
    return 1 if hard > a.baseline else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
