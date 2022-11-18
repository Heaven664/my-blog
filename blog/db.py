import sqlite3
import click
from flask import current_app, g


def get_db():
  """Sets connection to database if it hasn't been set yet"""
  if 'db' not in g:
    g.db = sqlite3.connect(
      current_app.config['DATABASE'],
      detect_types=sqlite3.PARSE_DECLTYPES
    )
    g.db.row_factory = sqlite3.Row

    return g.db 


def close_db(e=None):
  """Closes connection to database"""
  db = g.pop('db', None)

  if db is not None:
    db.close()


def init_db():
  """Initiates a database"""
  db = get_db()

  with current_app.open_resource('schema.sql') as f:
    db.executescript(f.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
  """Clears the existing data and create new tables"""
  init_db()
  click.echo('Initialized the database!')


def init_app(app):
  # Calls 'close_db' after returning a response
  app.teardown_appcontext(close_db)
  # Adds new command, that can be called with the 'flask'
  app.cli.add_command(init_db_command)