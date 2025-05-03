#!/bin/bash
SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR/.."
sam sync --stack-name aws-tagger-prod --config-env prod --profile romeubertho