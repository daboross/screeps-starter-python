#!/bin/bash
# Build file for transpiling Python files into JavaScript, and subsequently deploying to the screeps server.

# Fail early
set -e

# Base directory: the directory this script is in
BASEDIR="$(readlink -f $(dirname $0))"
# Python source directory
SRC_DIR="$BASEDIR/src"
# JavaScript source directory
JS_DIR="$BASEDIR/js_files"
# Final distribution directory
DIST_DIR="$BASEDIR/dist"

if [[ ! -e "$BASEDIR/env" ]]; then
    cd "$BASEDIR"
    virtualenv -p python3.5 --system-site-packages env
    "$BASEDIR/env/bin/pip" install -r "$BASEDIR/requirements.txt"
    npm install # do this here because this means we're in a new install
fi

# Transcrypt binary
TRANSCRYPT="$BASEDIR/env/bin/transcrypt"
# Grunt binary
GRUNT="$BASEDIR/node_modules/grunt-cli/bin/grunt"

cd "$SRC_DIR"
"$TRANSCRYPT" -n -b -p .none main.py
cd "$BASEDIR"

rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR/"

cp "$SRC_DIR/__javascript__/main.js" "$DIST_DIR/"
if [[ -e "$JS_DIR" ]]; then
    cp "$JS_DIR/"*.js "$DIST_DIR/"
fi

"$GRUNT" screeps "$@"
