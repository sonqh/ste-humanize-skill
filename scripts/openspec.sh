#!/usr/bin/env bash
# The one place that names the OpenSpec version. REQ-SKILL-014
set -euo pipefail
OPENSPEC_VERSION=2.0.0
exec npx -y "@fission-ai/openspec@$OPENSPEC_VERSION" "$@"
