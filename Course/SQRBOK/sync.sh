#!/usr/bin/env bash
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$HERE/../.." && pwd)"
SOURCE="$HERE/source"
UPSTREAM="https://github.com/sqrbok/sqrbok-preview.git"

# Refresh through Git only when the source is recorded as a gitlink. A
# .gitmodules entry alone is not enough while this integration is being added.
if [[ "$(git -C "$REPO_ROOT" ls-files --stage -- Course/SQRBOK/source 2>/dev/null)" == 160000\ * ]]; then
  git -C "$REPO_ROOT" submodule update --init --remote --depth 1 Course/SQRBOK/source || true
fi

# The downloadable Notes archive does not carry git-submodule contents, so make
# the refresh command useful there too by falling back to a shallow clone.
if [[ ! -d "$SOURCE/content" ]]; then
  if [[ -d "$SOURCE" ]] && [[ -n "$(ls -A "$SOURCE" 2>/dev/null || true)" ]]; then
    echo "SQRBOK source directory exists but is not a valid checkout: $SOURCE" >&2
    exit 2
  fi
  rm -rf "$SOURCE"
  git clone --depth 1 "$UPSTREAM" "$SOURCE"
elif [[ -d "$SOURCE/.git" ]]; then
  git -C "$SOURCE" pull --ff-only || true
fi

python3 "$HERE/tools/build_flashcards.py" \
  --source "$SOURCE" \
  --manifest "$HERE/source_manifest.json" \
  --output-dir "$HERE"
