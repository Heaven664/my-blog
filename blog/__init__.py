import os
from flask import Flask

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'myblog.sqlite'),
  )

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  @app.route("/")
  def hello():
    return "It's homepage of MyBlog"
  
  from . import db
  db.init_app(app)


  return app