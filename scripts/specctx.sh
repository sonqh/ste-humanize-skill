#!/usr/bin/env bash
# The one place that names the spec-ctx install source.
# Until the npm release, spec-ctx comes from git, pinned to a short commit SHA.
set -euo pipefail
SPECCTX_REF=f5a901fe340f
exec npx -y "github:sonqh/spec-ctx#$SPECCTX_REF" "$@"
