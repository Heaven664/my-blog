from flask import (
  Blueprint, Flask, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort 

from blog.auth import login_required
from blog.db import get_db

bp = Blueprint('blog', __name__)


@bp.route('/')
def index():
  return render_template('index.html')


@bp.route('/create', methods = ["GET", "POST"])
def create():
  return render_template('create.html')