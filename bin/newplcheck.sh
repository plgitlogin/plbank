rootdir=$(git rev-parse --show-toplevel)

for i in $*
do
    if [ $i = $0 ]
        then
            continue
    fi

    touch $rootdir/../../server/serverpl/tmp_test.py

    cat > $rootdir/../../server/serverpl/tmp_test.py <<EOF
from pysrc.newcheck import checkplfile, checkpltpfile
from gitload.loader import loadPL, loadPLTP
from gitload.models import Repository
from pleditor import PlFactory, pythonlangdata

import pytest, hashlib
import os
import json

EOF
    echo "Creating test for: "$i
    
    if [ ${i#*.} = "pl" ]
    # Writing testpl in the file 
    then
        cat >> $rootdir/../../server/serverpl/tmp_test.py <<EOF
@pytest.mark.django_db
def test_checkplfile():
    if ":" in "$i":
        r = Repository(name='$i'.split(':')[0],url='elsewhere',version=1)
    else:
        r = Repository(name=os.path.basename('$rootdir'),url='elsewhere',version=1)
        
    assert(checkplfile('$i', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))
EOF
        pytest $rootdir/../../server/serverpl/tmp_test.py
        # Test was collected and passed successfully
        if [ $? -eq 0 ]
        then
            git commit -m " newcheck commit " $i
            echo "commit "$i
            rm $rootdir/../../server/serverpl/tmp_test.py
        fi
    elif [ ${i#*.} = "pltp" ]
    #Writing testpltp in the file 
    then
        cat >> $rootdir/../../server/serverpl/tmp_test.py <<EOF
@pytest.mark.django_db
def test_checkpltpfile():
    r = Repository(name=os.path.basename('$rootdir'),url='elsewhere',version=1)
    assert(checkpltpfile('$i', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))
EOF
        pytest $rootdir/../../server/serverpl/tmp_test.py
        # Test was collected and passed successfully
        if [ $? -eq 0 ]
        then
            pltp=$i
            rm $rootdir/../../server/serverpl/tmp_test.py
            echo "relance"
            #Get all the pl in the current pltp removing the "@ " and apply the command on them 
            grep "^@" $i  | sed -e "s/^@ /*//" | xargs newplcheck.sh
            echo "commit "$i
            git commit -m " newcheck commit " $i
        elif [ $? -eq 1 ]
        then
            echo "Tests were collected and run but some of the tests failed"
        fi
    else
        echo $i" n'est pas un fichier conforme" 
        rm $rootdir/../../server/serverpl/tmp_test.py
        continue
    fi

done

git push
