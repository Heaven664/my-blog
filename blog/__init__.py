import os
from flask import Flask, session
from . import db

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
    return f"Hello world!"
  
  from . import db
  db.init_app(app)

  from . import auth
  app.register_blueprint(auth.bp)

  return app