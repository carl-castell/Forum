
from flask import Blueprint, render_template, redirect, url_for, send_file
from app.users.models import User


blueprint = Blueprint('simple_pages', __name__)

@blueprint.route('/')
def index():
  return render_template('index.html')

#for google verification
@blueprint.route("/google-provided.html")
def google_site_verf():
    return render_template("google.html")
