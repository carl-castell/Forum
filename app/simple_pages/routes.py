
from flask import Blueprint, render_template, redirect, url_for, send_file
from app.users.models import User
from os import environ

secret= "/",environ['DATABASE_URL']

blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('index.html')

#for google verification
@blueprint.route(secret)
def google_site_verf():
    return url_for('/etc/secrets/google')
