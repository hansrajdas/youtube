#!/bin/bash

set -x
export num=1143
export level=medium
export problem="longest-common-subsequence"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
