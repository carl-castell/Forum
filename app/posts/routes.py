from flask import Blueprint, render_template
from .models import Topic
from flask_login import login_required

blueprint = Blueprint('posts', __name__)

@blueprint.get('/topics')
@login_required
def topics():
    return render_template('posts/overview.html')