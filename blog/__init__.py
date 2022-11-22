import os
from flask import Flask, g, flash, request, redirect, url_for, render_template
from .auth import login_required
from werkzeug.utils import secure_filename

counter = 0

def create_app():
  
  app = Flask(__name__, instance_relative_config=True)

  UPLOAD_FOLDER = os.path.join(app.instance_path, 'images/')

  app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

  app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'myblog.sqlite'),
  )

  try:
    os.makedirs(app.instance_path)
  except OSError:
    pass
  
  @app.route("/hello")
  @login_required
  def hello():
    name = g.user['username']
    return f"Hello {name}!"

  from . import db
  db.init_app(app)

  from . import auth
  app.register_blueprint(auth.bp)

  from . import blog
  app.register_blueprint(blog.bp)
  app.add_url_rule('/', endpoint='index')

  from .blog import allowed_file
  
  @app.route('/create', methods = ["GET", "POST"])
  @login_required
  def create():
    if request.method == "POST":
      file = request.files['file']
      if file and allowed_file(file.filename):
        global counter
        counter += 1
        filename = str(counter) + secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template('create.html')
  

  return app