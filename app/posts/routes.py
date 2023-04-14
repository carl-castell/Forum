from flask import Blueprint, render_template, current_app, request, redirect, url_for
from .models import Topic
from app.users.models import User
from flask_login import login_required, current_user
from app.extensions.database import db

blueprint = Blueprint('posts', __name__)

@blueprint.get('/topics')
#@login_required
def topics():
    topics = db.session.query(Topic, User).filter(Topic.author_id == User.id).all()
    return render_template('topics/index.html',topics=topics)


@blueprint.get('/topics/new')
#@login_required
def new_topic():
    return render_template('posts/new_topic.html')

@blueprint.post('/topics/new')
#@login_required
def post_new_topic():
  
    new_topic = Topic(
        title=request.form.get('title'),
        description=request.form.get('description'),
        author_id=current_user.id
    )
    new_topic.save()
    
    return redirect(url_for('posts.topics'))

@blueprint.get('/topics/show/<id>')
def get_topic_show(id):
    topic= Topic.query.filter_by(id=id).first_or_404()
    topic_new = db.session.query(Topic, User).filter(Topic.id == id).filter(Topic.author_id == User.id).first()
    return render_template('topics/show.html',topic_new=topic_new)