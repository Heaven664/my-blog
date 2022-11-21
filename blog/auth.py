import functools
from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash
from blog.db import get_db


bp = Blueprint('auth', __name__, url_prefix="/auth")

@bp.route('/register', methods = ["GET", "POST"])
def register():
  if request.method == "POST":
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    error = None

    if not username:
      error = "Please provide username!"
    
    elif not password:
      error = "Please provide password!"

    if error is None:
      try:
        db.execute(
          "INSERT INTO user (username, password) VALUES (?, ?)",
          (username, generate_password_hash(password))
        )
        db.commit()

      except db.IntegrityError:
        error = f"User {username} is already registered!"

      else:
        return render_template('register.html')
    
    flash(error)

    return redirect(url_for("auth.login"))

  else:
    return render_template('register.html')