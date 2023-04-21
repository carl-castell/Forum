from flask import Blueprint, render_template, current_app, request, redirect, url_for
from .models import Topic, Reply
from app.users.models import User
from flask_login import login_required, current_user
from app.extensions.database import db
from app.extensions.authentication import login_manager

blueprint = Blueprint('posts', __name__)


################# index route ###############################################
@blueprint.get('/topics')
@login_required
def topics():
    topics = db.session.query(Topic, User).filter(Topic.author_id == User.id).all()
    return render_template('topics/index.html',topics=topics)


################# add new topic #############################################
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


################# show content ###############################################
@blueprint.get('/topics/show/<int:id>')
@login_required
def get_topic_show(id):
    topic_new = db.session.query(Topic, User).filter(Topic.id == id).filter(Topic.author_id == User.id).first()
    replies = db.session.query(Reply, User).filter(Reply.topic_id == id).filter(Reply.author_id == User.id).all()
    return render_template('topics/show.html',topic_new=topic_new ,replies=replies)


################# add reply ##################################################
@blueprint.post('/topics/show/<id>')
@login_required
def reply(id):
    new_reply = Reply(
        reply_content =request.form.get('description'),
        author_id=current_user.id,
        topic_id=id
    )
    
    new_reply.save()
    
    return redirect(f'/topics/show/{id}')


################# delete topic with replys ####################################
@blueprint.get('/topics/delete/<id>')
@login_required
def delete_topic(id):
    topic_to_delete = Topic.query.filter_by(id=id).first()
    replys_to_delete = Reply.query.filter_by(topic_id=id).all()
    topic_to_delete.delete()
    for item in replys_to_delete:
        item.delete()
    return redirect(url_for('posts.topics'))


################# delete reply ################################################


################# authorized handler ##########################################
@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('users.get_login'))


################## Edit topics ################################################
@blueprint.get('/topics/edit/<int:id>')
#@login_required
def get_topic_edit(id):
    change_topic = db.session.query(Topic, User).filter(Topic.id == id).filter(Topic.author_id == User.id).first()
    return render_template('posts/edit_topic.html', change_topic=change_topic)


@blueprint.post('/topics/edit/<int:id>')
#@login_required
def post_topic_edit(id):
    
    update_topic = db.session.query(Topic).filter(Topic.id==id).first()
    
    update_topic.title=request.form.get('title')
    update_topic.description=request.form.get('description')
    update_topic.author_id=current_user.id

    
    update_topic.save()
    
    
    return redirect(f'/topics/show/{id}')

################## Edit replys ################################################
@blueprint.get('/topics/reply/edit/<int:id>')
#@login_required
def get_reply_edit(id):
    return render_template('posts/new_topic.html')

@blueprint.post('/topics/reply/edit/<int:id>')
#@login_required
def post_reply_edit(id):
    return redirect(url_for('posts.topics'))