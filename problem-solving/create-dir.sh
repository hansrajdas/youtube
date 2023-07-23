#!/bin/bash

set -x
export num=188
export level=hard
export problem="best-time-to-buy-and-sell-stock-iv"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
