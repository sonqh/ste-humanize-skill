#!/usr/bin/env bash
# The one place that names the spec-ctx install source.
set -euo pipefail
SPECCTX_VERSION=0.1.0
exec npx -y "spec-ctx@$SPECCTX_VERSION" "$@"
