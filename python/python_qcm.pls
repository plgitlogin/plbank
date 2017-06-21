# Copyright 2016 Coumes Quentin
# Strategy for a python exercise with a QCM

template=/python/python.pls

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
                {% if feedback.grade.success == True and not feedback.plateform_error %}
                    <div class="alert alert-success">
                        {{ feedback.grade.feedback|safe }}
                    </div>
                {% elif feedback.grade.success == True and feedback.plateform_error %}
                    <div class="alert alert-info">
                        {{ feedback.grade.feedback|safe }}
                    </div>
                {% else %}
                    <div class="alert alert-danger">
                        {{ feedback.grade.feedback|safe }}
                    </div>
                {% endif %}
            {% endif %}
            
            <form action="" method="post">
                {% csrf_token %}
                <center>
                    {% for item in pl.answer %}
                        <label class="checkbox-inline">
                          <input type="checkbox" value="item">item
                        </label>
                    {% endfor %}
                </center>
                <center><button class="btn btn-primary" type="submit">Valider</button></center>
            </form>
        </div>
    </div>
==
