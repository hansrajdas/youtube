#!/bin/bash

set -x
export num=198
export level=medium
export problem="house-robber"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
