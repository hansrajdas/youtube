#!/bin/bash

set -x
export num=123
export level=hard
export problem="best-time-to-buy-and-sell-stock-iii"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
