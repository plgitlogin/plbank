#!/bin/bash
rootdir=$(git rev-parse --show-toplevel)

checking ()
{
    # nb of pl/pltp valid
    nb_pl=0
    nb_pltp=0
    for i in $*
    do
        touch $rootdir/../../server/serverpl/test_tmp.py

        cat > $rootdir/../../server/serverpl/test_tmp.py <<EOF
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
            cat >> $rootdir/../../server/serverpl/test_tmp.py <<EOF
@pytest.mark.django_db
def test_checkplfile():
    if ":" in "$i":
        r = Repository(name='$i'.split(':')[0],url='elsewhere',version=1)
    else:
        r = Repository(name=os.path.basename('$rootdir'),url='elsewhere',version=1)
        
    assert(checkplfile('$i', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))
EOF
            pytest $rootdir/../../server/serverpl/test_tmp.py
            # Test was collected and passed successfully
            if [ $? -eq 0 ]
            then
                let "nb_pl+=1"
                git commit -m " newcheck commit " $i
                echo "commit "$i
                rm $rootdir/../../server/serverpl/test_tmp.py
            else
                echo "Test "$i" failed"
                rm $rootdir/../../server/serverpl/test_tmp.py
            fi
        elif [ ${i#*.} = "pltp" ]
        #Writing testpltp in the file 
        then
            cat >> $rootdir/../../server/serverpl/test_tmp.py <<EOF
@pytest.mark.django_db
def test_checkpltpfile():
    r = Repository(name=os.path.basename('$rootdir'),url='elsewhere',version=1)
    assert(checkpltpfile('$i', r, sandboxurl = 'http://127.0.0.1:8000/sandbox/?action=execute'))
EOF
            pytest $rootdir/../../server/serverpl/test_tmp.py
            # Test was collected and passed successfully
            if [ $? -eq 0 ]
            then
                pltp=$i
                rm $rootdir/../../server/serverpl/test_tmp.py
                echo "check des pl de "$i
                #Get all the pl in the current pltp removing the "@ " and apply the command on them 
                args=$(grep "^@" $i  | sed -e "s/^@ \/*//")
                echo $args
                checking $args
                echo "commit "$i
                let "nb_pltp+=1"
                git commit -m " newcheck commit " $i
            elif [ $? -eq 1 ]
            then
                echo "Tests were collected and run but some of the tests failed"
                rm $rootdir/../../server/serverpl/test_tmp.py
            fi
        else
            echo $i" n'est pas un fichier conforme" 
            rm $rootdir/../../server/serverpl/test_tmp.py
            continue
        fi

    done
}
    
    checking $@
    
    if [ $nb_pl -gt 0 ]
    then
        echo "Ajout de "$nb_pltp" pltp et "$nb_pl" pl"
        git push
    fi
