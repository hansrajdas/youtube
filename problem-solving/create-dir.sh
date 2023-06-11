#!/bin/bash

set -x
export num=1220
export level=hard
export problem="count-vowels-permutation"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
