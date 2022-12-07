import os
from flask import (
  Blueprint, Flask, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from blog.auth import login_required
from blog.db import get_db
from . import create_app

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
  db = get_db()

  posts = db.execute(
    "SELECT * FROM post ORDER BY created DESC"
  ).fetchall()
  db.commit()
  return render_template("index.html", posts=posts)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
          

def get_post(id, check_author=True):
  post = get_db().execute(" SELECT p.id, title, body, created, author_id, username \
                            FROM post p JOIN user u ON p.author_id = u.id \
                            WHERE p.id = ?", (id,)).fetchone()
  if post is None:
    abort(404, f"Post id {id} doesn't exist")

  if check_author and post['author_id'] != g.user['id']:
    abort(403)

  return post
