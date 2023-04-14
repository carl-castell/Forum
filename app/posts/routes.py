from flask import Blueprint, render_template, current_app, request, redirect, url_for
from .models import Topic
from flask_login import login_required, current_user

blueprint = Blueprint('posts', __name__)

@blueprint.get('/topics')
#@login_required
def topics():
    topics=Topic.query.all()
    user=current_user.email
    return render_template('topics/index.html',topics=topics,user=user)


#@blueprint.get('/topics/show')
#@login_required
#def show_topic():
#    return render_template('topics/index.html')

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
        author_id=request.form.get(current_user)
    )
    new_topic.save()
    
    return redirect(url_for('posts.topics'))