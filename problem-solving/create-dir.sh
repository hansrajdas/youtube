#!/bin/bash

set -x
export num=312
export level=hard
export problem="burst-balloons"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
