#!/bin/bash

set -x
export num=647
export level=medium
export problem="palindromic-substrings"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
