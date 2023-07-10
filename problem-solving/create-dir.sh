#!/bin/bash

set -x
export num=115
export level=hard
export problem="distinct-subsequences"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
