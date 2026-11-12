#!/usr/bin/env bash
# The one place that names the spec-ctx install source. REQ-SKILL-013
set -euo pipefail
SPECCTX_VERSION=0.6.0
exec npx -y "spec-ctx@$SPECCTX_VERSION" "$@"
