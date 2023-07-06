#!/bin/bash

set -x
export num=72
export level=medium
export problem="edit-distance"

mkdir _lc-$(printf '%04s\n' $num)-$level-$problem
