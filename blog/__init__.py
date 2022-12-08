import os
from flask import Flask, g, flash, request, redirect, url_for, render_template, session
from .auth import login_required
from werkzeug.utils import secure_filename
from PIL import Image

counter = 0

def create_app():
  
  app = Flask(__name__, instance_relative_config=True)

  UPLOAD_FOLDER = os.path.join(app.static_folder, 'images/')

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
      title = request.form['title']
      text = request.form['text']
      error = None
      base = db.get_db()
      id = session['user_id']

      author = base.execute(
        "SELECT username FROM user WHERE id = ?", (id,)
      ).fetchone()[0]

      author = str(author)

      if not author:
        error = "Can't recognize user"

      if not title:
        error = "Please provide title!"
      
      if not text:
        error = "Please provide text!"

      if file and allowed_file(file.filename):
        global counter
        counter += 1
        filename = secure_filename(file.filename)
        filename = str(counter) + '.' + filename.rsplit(".", 1)[1].lower()
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        img = Image.open(filepath)
        width = img.width
        heigh = img.height

        if (width / heigh) > 0.5 and (width / heigh) < 3:
          path = filename
          if error is None:
            base.execute(
            "INSERT INTO post (author_id, title, body, image_path, author_name) VALUES (?, ?, ?, ?, ?)",
            (session['user_id'], title, text, path, author),
          )
            base.commit() 
            return redirect(url_for('index'))
        else:
          os.remove(filepath)
          error = "Image dimensions are not allowed"

      elif not file:
        if error is None:
          base.execute(
          "INSERT INTO post (author_id, title, body, author_name) VALUES (?, ?, ?, ?)",
          (session['user_id'], title, text, author),
        )
          base.commit()
          return redirect(url_for('index'))

      else:
        error = 'Unsupported file extension!'

      flash(error)


    return render_template('create.html')


  from .blog import get_post
  from .db import get_db

  @app.route("/<int:id>/delete", methods = ["POST"])
  @login_required
  def delete(id):
    get_post(id)
    db = get_db()
    image = db.execute("SELECT image_path FROM post WHERE id = ?", (id,)).fetchone()[0]

    if image:
      path = os.path.join(UPLOAD_FOLDER, str(image))
      os.remove(path)

    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('index'))
  
  return app