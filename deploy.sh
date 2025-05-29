#!/bin/bash

# Exit on error
set -e

echo "Cleaning previous builds..."
make clean
rm -rf build/html

echo "Building Sphinx documentation..."
sphinx-build -b html . build/html

echo "Publishing to GitHub Pages..."
ghp-import -n -p -f build/html

echo "✅ Deployment complete! Visit your site:"
echo "https://alexta0.github.io/gt_tutorial/"
