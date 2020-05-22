import os

os.environ["SECRET_KEY"] = "Start1ing_p01nt"

from os import path
if path.exists("env.py"):
  import env 

SECRET_KEY = os.environ.get('SECRET_KEY')