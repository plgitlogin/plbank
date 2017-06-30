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
<<<<<<< HEAD


form==
    {% csrf_token %}
    <!-- Do not tabulate this div as the tabulation will appear in the editor -->
    <div id="editor" style="border-width: 1px; border-color: #5bc0de; border-radius: 4px;">
{% if answer_exists %}{{ anwser }}{% else %}{{ pl.code }}{% endif %}</div>
    <input type="hidden" name="code" style="display: none;">
    <br>
    <script src="/static/AceCodeEditor/ace-builds/ace-builds-master/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
    <script>
        var editor = ace.edit('editor');
            editor.session.setMode("ace/mode/python");
            editor.setTheme("ace/theme/vibrant_ink");
        
        var input = $('input[name="code"]');
            editor.getSession().on("change", function() {
            input.val(editor.getSession().getValue());
        });
    </script
==
=======
>>>>>>> 14d1a883c8651e12b17d5d35e29d6eda556573a7
>>>>>>> b96c947de99ad4bc419ebabd6589e996869bc51b
