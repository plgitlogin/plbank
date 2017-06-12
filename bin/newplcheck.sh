rootdir=$(git rev-parse --show-toplevel)

for i
do
    if [ $i == 0 ]
        then
            continue
    fi
if [ ${i#*.} == "pl" ]
    then
        touch $rootdir/../../server/serverpl/tmp_test.py

        echo "from pysrc.newcheck import checkplfile, checkpltpfile
from gitload.loader import loadPL, loadPLTP
from gitload.models import Repository
from pleditor import PlFactory, pythonlangdata


import pytest, hashlib

import os
import json

@pytest.mark.django_db
def test_checkplfile():
    r = Repository(name=os.path.basename('"$rootdir"'),url='elsewhere',version=1)
    pl, warning = loadPL('"$i"', r, PLF=PlFactory(langdata=pythonlangdata))
    print(warning)
    assert pl != None
    assert(checkplfile(pl.rel_path, r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))" > $rootdir/../../server/serverpl/tmp_test.py
    
    elif [ ${i#*.} == "pltp" ]
        then
        echo "from pysrc.newcheck import checkplfile, checkpltpfile
from gitload.loader import loadPL, loadPLTP
from gitload.models import Repository
from pleditor import PlFactory, pythonlangdata


import pytest, hashlib

import os
import json

@pytest.mark.django_db
def test_checkpltpfile():
    r = Repository(name=os.path.basename('"$rootdir"'),url='elsewhere',version=1)
    pltp, warning = loadPLTP('"$i"', r, PLF=PlFactory(langdata=pythonlangdata))
    print(warning)
    assert pltp != None
    assert(checkpltpfile(pltp.rel_path, r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))" > $rootdir/../../server/serverpl/tmp_test.py

    else
        echo "type de fichier inconnu" 
        break
fi
    
    pytest $rootdir/../../server/serverpl/tmp_test.py
    
done

rm $rootdir/../../server/serverpl/tmp_test.py
