from app.extensions.database import db, CRUDMixin
from datetime import datetime

class Topic(db.Model, CRUDMixin):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(200))
  description = db.Column(db.Text())
  date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  
  
  