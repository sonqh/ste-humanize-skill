#!/usr/bin/env bash
# The CI jobs, run on this machine before a push. The pre-push hook calls it.
set -uo pipefail
cd "$(dirname "$0")/.."
log=$(mktemp)
trap 'rm -f "$log"' EXIT
steps=(
  'bash scripts/specctx.sh gate --strict --markdown "CLAUDE.md AGENTS.md decisions/*.md openspec/**/*.md docs/**/*.md"'
  'python3 -m unittest discover -s tests'
  'python3 scripts/tells-lint.py --selftest'
  'python3 scripts/ste-lint.py --selftest'
)
for s in "${steps[@]}"; do
  echo "ci-local: $s"
  if ! bash -c "$s" > "$log" 2>&1; then
    tail -40 "$log"
    echo "ci-local: fail: $s"
    exit 1
  fi
done
echo "ci-local: ok, ${#steps[@]} steps"
