# Copyright 2016 Coumes Quentin
# Default strategy for a python exercise, a strategy inheriting this one need to declare a 'pl=='

css==
    <link rel="stylesheet" type="text/css" href="{% static 'playexo/css/exo_info.css' %}" />
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
