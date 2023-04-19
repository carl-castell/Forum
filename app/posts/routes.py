from flask import Blueprint, render_template, current_app, request, redirect, url_for
from .models import Topic, Reply
from app.users.models import User
from flask_login import login_required, current_user
from app.extensions.database import db
from app.extensions.authentication import login_manager

blueprint = Blueprint('posts', __name__)


#Route to index all topics
@blueprint.get('/topics')
@login_required
def topics():
   # page = request.args.get('page', 1, type=int)
   # topics_pagination = Topic.query.paginate(page=page, per_page=current_app.config['TOPICS_PER_PAGE'])
    topics = db.session.query(Topic, User).filter(Topic.author_id == User.id).all()
    return render_template('topics/index.html',topics=topics)


#Route to add a new topic
@blueprint.get('/topics/new')
@login_required
def new_topic():
    return render_template('posts/new_topic.html')

@blueprint.post('/topics/new')
@login_required
def post_new_topic():
  
    new_topic = Topic(
        title=request.form.get('title'),
        description=request.form.get('description'),
        author_id=current_user.id
    )
    new_topic.save()
    
    return redirect(url_for('posts.topics'))


#Route to show a topic in full detail
@blueprint.get('/topics/show/<int:id>')
@login_required
def get_topic_show(id):
    topic_new = db.session.query(Topic, User).filter(Topic.id == id).filter(Topic.author_id == User.id).first()
    #replies = db.session.query(Reply).filter(Reply.topic_id == id).all()
    return render_template('topics/show.html',topic_new=topic_new) #,replies=replies)

@blueprint.post('/topics/show/<id>')
@login_required
def reply(id):

    new_reply = Reply(
        reply_content =request.form.get('description'),
        author_id=current_user.id,
        topic_id=id
    )
    
    new_reply.save()
    
    return redirect(url_for('posts.topics'))

#delete feature(needs to be fixed)
@blueprint.get('/topics/delete/<id>')
@login_required
def delete_topic(id):
    topic = Topic.query.filter_by(id=id).first()
    topic.delete()
    return redirect(url_for('posts.topics'))

#Route that redirects user to log in page if they try to gain unathorized access
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('users.get_login'))