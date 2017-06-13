rootdir=$(git rev-parse --show-toplevel)

touch $rootdir/../../server/serverpl/tmp_test.py

        echo "from pysrc.newcheck import checkplfile, checkpltpfile
from gitload.loader import loadPL, loadPLTP
from gitload.models import Repository
from pleditor import PlFactory, pythonlangdata


import pytest, hashlib

import os
import json" > $rootdir/../../server/serverpl/tmp_test.py

let "j = 0"

for i
do
    if [ $i == 0 ]
        then
            continue
    fi
if [ ${i#*.} == "pl" ]
    then
        echo "@pytest.mark.django_db
def test_checkplfile"$j"():
    r = Repository(name=os.path.basename('"$rootdir"'),url='elsewhere',version=1)
    assert(checkplfile('"$i"', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))" >> $rootdir/../../server/serverpl/tmp_test.py
    
    let "j += 1"
    
    elif [ ${i#*.} == "pltp" ]
        then
            echo "@pytest.mark.django_db
def test_checkpltpfile"$j"():
    r = Repository(name=os.path.basename('"$rootdir"'),url='elsewhere',version=1)
    assert(checkpltpfile('"$i"', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))" >> $rootdir/../../server/serverpl/tmp_test.py
    
    let "j += 1"
    
    else
        echo $i" n'est pas un fichier conforme" 
        continue
fi
        
done

pytest $rootdir/../../server/serverpl/tmp_test.py

rm $rootdir/../../server/serverpl/tmp_test.py
