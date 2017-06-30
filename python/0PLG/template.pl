# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>

# using the new plgrader 

name=/python/0PLG/template.pl

grader==
from plgrader import Grader
g=Grader()
print(g.grade())
==


sandbox=@/pysrc/src/__init__.py
sandbox=@/pysrc/src/plgrader.py
sandbox=@/pysrc/src/feedback.py
files=@/pysrc/src/__init__.py
files=@/pysrc/src/plgrader.py
files=@/pysrc/src/feedback.py

type=sandbox


evaluator==
sandbox = get_object_or_404(Sandbox, name="php-sandbox")
try:
    sandbox_session = SandboxSession(pl, request.POST['code'], sandbox.url)
    feedback = json.loads(sandbox_session.call())
    if feedback['grade']['success']:
        state = Answer.SUCCEEDED
    else:
        state = Answer.STARTED
    Answer(value=request.POST['code'], pl=pl, user=request.user, state=state).save()
    if feedback['grade']['success']:
        return True, feedback
    return False, feedback
except Exception as e:
    return True, str(type(e))+": "+ str(e))
==
>>>>>>> 14d1a883c8651e12b17d5d35e29d6eda556573a7
