#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
PROJECTDIR="$PWD/$BASEDIR/../"

PYTHONPATH=$PROJECTDIR /usr/bin/python3.6 $PROJECTDIR/tests/test_calculate_npmi.py
