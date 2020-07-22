from inspect import getsourcefile
import os.path
import sys

try:
    PATH = sys.path[:]
    current_dir = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
    sys.path.insert(0, current_dir)
    from echo import db, app
finally:
    sys.path = PATH

with app.app_context():
    db.create_all()
