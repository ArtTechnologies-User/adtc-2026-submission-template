#!/usr/bin/env bash
# Download your model weight file.
#
# Rules:
#   - Must be idempotent (safe to run multiple times).
#   - Must download without any credentials (public URL only).
#   - The output path must match `_runtime.model_path` in metadata.json.

#!/bin/bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MODEL_DIR="$HERE/model"
MODEL_FILE="$MODEL_DIR/WAEC-Tutor-Q4_K_M.gguf"

# ── Updated: Google Drive model weight URL ────────────────────────────────
FILE_ID="1nN5lDd7BNarbkofKwAiYX8FLleGQV03J"
MODEL_URL="https://drive.google.com/uc?export=download&id=$FILE_ID"
# ─────────────────────────────────────────────────────────────────────────

mkdir -p "$MODEL_DIR"

if [[ -f "$MODEL_FILE" ]]; then
  echo "model already present at $MODEL_FILE — skipping download"
  exit 0
fi

echo "downloading $MODEL_URL → $MODEL_FILE (~2.8 GB)…"

if command -v gdown > /dev/null 2>&1; then
  gdown --id "$FILE_ID" -O "$MODEL_FILE"
elif command -v curl > /dev/null 2>&1; then
  curl -L --fail --progress-bar -o "$MODEL_FILE.partial" "$MODEL_URL"
  mv "$MODEL_FILE.partial" "$MODEL_FILE"
elif command -v wget > /dev/null 2>&1; then
  wget --show-progress -O "$MODEL_FILE.partial" "$MODEL_URL"
  mv "$MODEL_FILE.partial" "$MODEL_FILE"
else
  echo "error: neither gdown, curl, nor wget found" >&2
  exit 1
fi

echo "✅ done: $MODEL_FILE"


