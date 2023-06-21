#!/bin/bash

set -x
export num=375
export level=medium
export problem="guess-number-higher-or-lower-ii"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
