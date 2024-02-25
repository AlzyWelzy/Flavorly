{% extends "base.html" %}

{% block page_title %}
Update Recipe
{% endblock %}

{% load crispy_forms_tags %}

{% block content %}
    <div class="container mt-5">
        <div class="row justify-content-center">
            <div class="col-md-6">
                <form method="post" class="form-group" enctype="multipart/form-data">
                    {% csrf_token %}
                    {{ form|crispy }}

                    <button type="submit" class="btn btn-success">Update</button>
                </form>
            </div>
        </div>
    </div>
{% endblock %}
