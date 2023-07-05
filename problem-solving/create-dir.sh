#!/bin/bash

set -x
export num=516
export level=medium
export problem="longest-palindromic-subsequence"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
