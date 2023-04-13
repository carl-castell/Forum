from flask import Blueprint, render_template
from .models import Topic

blueprint = Blueprint('posts', __name__)

@blueprint.get('/topics')
def topics():
    return render_template('posts/overview.html')