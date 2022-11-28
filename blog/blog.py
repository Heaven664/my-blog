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
    "SELECT * FROM post ORDER BY created"
  ).fetchall()
  db.commit()
  return render_template("index.html", posts=posts)


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS