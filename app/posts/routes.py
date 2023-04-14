from flask import Blueprint, render_template, current_app, request
from .models import Topic
from flask_login import login_required

blueprint = Blueprint('posts', __name__)

@blueprint.get('/topics')
#@login_required
def topics():
    return render_template('topics/index.html')


@blueprint.get('/topics/show')
#@login_required
def show_topic(id):
    return render_template('topics/index.html')

@blueprint.get('/topics/new')
#@login_required
def new_topic():
    return render_template('posts/new_topic.html')