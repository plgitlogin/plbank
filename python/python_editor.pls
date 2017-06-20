# Copyright 2016 Coumes Quentin
# Strategy for a python exercise with an editor


css==
    <link rel="stylesheet" type="text/css" href="{% static 'playexo/css/exo_info.css' %}" />
==

pl==

<div class="panel panel-primary">
        <div class="panel-heading">
            <div class="col-md-4 text-left"></div>
            <div class="col-md-4 text-center"><h3>{% if 'title' in pl %}{{ pl.title }}{% endif %}</h3></div>
            <div class="col-md-4 text-right">{% if 'author' in pl %}{{ pl.author }}{% endif %}</div>
            <br>
            <br>
            <br>
        </div>
        
        <div class="panel-body">
            {{ pl.text|markdown }}
            
            <hr>
            {% if feedback %}
                <div class="alert alert-info">
                    {{ feedback }}
                </div>
            {% endif %}
            <!-- Do not tabulate this div as the tabulation will appear in the editor -->
            <div id="editor" style="border-width: 1px; border-color: #5bc0de; border-radius: 4px;">
{% if answer_exists %}{{ anwser }}{% else %}{{ pl.code }}{% endif %}</div>
            
            <form action="" method="post">
                {% csrf_token %}
                <input type="hidden" name="code" style="display: none;">
                
                <br>
                <center>
                    <div class="btn-group">
                        <button class="btn btn-primary" type="submit" formaction="/playexo/form/{{ pltp_sha1 }}/{{ pl_sha1 }}/grade/"> Validation</button>
                        <button class="btn btn-secondary" type="submit" formaction="/playexo/form/{{ pltp_sha1 }}/{{ pl_sha1 }}/reset/"> Reset</button>
                        <button class="btn btn-warning" type="submit" formaction="/playexo/form/{{ pltp_sha1 }}/{{ pl_sha1 }}/undo/"> Précédent</button>
                    </div>
                </center>
            </form>
        </div>
    </div>

    <script src="/static/AceCodeEditor/ace-builds/ace-builds-master/src-noconflict/ace.js" type="text/javascript" charset="utf-8"></script>
    <script>
        var editor = ace.edit('editor');
            editor.session.setMode("ace/mode/python");
            editor.setTheme("ace/theme/vibrant_ink");

        var input = $('input[name="code"]');
            editor.getSession().on("change", function() {
            input.val(editor.getSession().getValue());
        });
    </script>
==



pltp==

<div class="panel panel-primary">
    <div class="panel-heading">
        <div class="col-md-4 text-left"></div>
        <div class="col-md-4 text-center"><h3>{% if 'title' in pltp %}{{ pltp.title }}{% endif %}</h3></div>
        <div class="col-md-4 text-right">{% if 'author' in pltp %}{{ pltp.author }}{% endif %}</div>
        <br>
        <br>
        <br>
    </div>
    
    <div class="panel-body">
        {% if "introduction" in pltp %}
                {{ pltp.introduction|markdown }}
        {% endif %}
    </div>
</div>

==



navigation==

    <div id="btn-group-toggle" class="btn-group">
        <!-- PLTP -->
        <a href="/playexo/add/activity/{{ activity_id }}" type="button" class="btn btn-default btn-lg">{{ pltp.name }}</a>
        <!-- Every PL -->
        {% for item  in pl_list %}
            {% if pl and pl_name == pl.name %}
                <a href="/playexo/add/pl/{{ activity_id }}/{{ item.sha1 }}" type="button" class="btn btn-info btn-lg active">{{ item.name }}</a>
            {% else %}
                <a href="/playexo/add/pl/{{ activity_id }}/{{ item.sha1 }}" type="button" class="btn btn-info btn-lg">{{ item.name }}</a>
            {% endif %}
        {% endfor %}

        <script>
            var wideScreen = 990;
            var toggleBtnGroup = function() {
                var windowWidth = $(window).width();
                  
                if(windowWidth > wideScreen) {
                    $('#btn-group-toggle').addClass('btn-group-vertical').removeClass('btn-group');
                } else {
                    $('#btn-group-toggle').addClass('btn-group').removeClass('btn-group-vertical');
                }
            }
            toggleBtnGroup(); // trigger on load
            window.addEventListener('resize',toggleBtnGroup); // change on resize
        </script>
    </div>

==
