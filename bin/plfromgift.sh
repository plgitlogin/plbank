#!/bin/bash
rootdir=$(git rev-parse --show-toplevel)
first_it=1
for i in $@
do
    if [ $first_it == 1 ]
    then
        path=$i
        first_it=0
        continue    
    fi
    python $rootdir/server/serverpl/gitload/pltpfromgift.py $path $i
done
