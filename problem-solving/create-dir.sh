#!/bin/bash

set -x
export num=122
export level=medium
export problem="best-time-to-buy-and-sell-stock-ii"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
