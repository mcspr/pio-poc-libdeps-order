#!/usr/bin/env bash

set -x -e -v

pio system info
rm -rf .pio/build
rm -rf .pio/libdeps
pio run -e $1
