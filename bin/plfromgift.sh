#!/bin/bash
rootdir=$(git rev-parse --show-toplevel)
for i in $@
do
    python $rootdir/server/serverpl/gitload/pltpfromgift.py $i
done
