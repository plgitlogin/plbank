# Copyright 2016 Dominique Revuz <dr@univ-mlv.fr>

# using the new plgrader 

name=/python/0PLG/template.pl

grader==
from plgrader import Grader
g=Grader()
print(g.grade())
==


type=sandbox


files=@/pysrc/src/__init__.py
files=@/pysrc/src/plgrader.py
files=@/pysrc/src/feedback.py


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
