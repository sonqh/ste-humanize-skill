#!/usr/bin/env bash
# Prints ok=true when CI can read the spec-ctx repository that scripts/specctx.sh names.
# The repository is private for now. Without access, CI skips the spec-ctx gate and the local gate stays the primary one.
set -euo pipefail
here=$(cd "$(dirname "$0")/.." && pwd)
repo=$(grep -oE 'github:[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+' "$here/scripts/specctx.sh" | head -1 | cut -d: -f2)
if GIT_TERMINAL_PROMPT=0 git ls-remote "https://github.com/$repo.git" HEAD >/dev/null 2>&1; then
  echo "ok=true"
else
  echo "spec-ctx gate skipped: repository not reachable from CI, run scripts/ci-local.sh" >&2
  echo "ok=false"
fi
