#!/bin/bash
# Usage: ./release.sh [release-notes]

set -e

# Extract version from pyproject.toml
VERSION=$(grep '^version' pyproject.toml | head -n1 | cut -d '"' -f2)
if [ -z "$VERSION" ]; then
  echo "Could not extract version from pyproject.toml."
  exit 1
fi

TAG="v$VERSION"
NOTES="${1:-Release $TAG: notebook usage docs, async examples, and robustness improvements}"

echo "Tagging and releasing $TAG"
git tag "$TAG"
git push origin "$TAG"
gh release create "$TAG" --title "$TAG" --notes "$NOTES"
