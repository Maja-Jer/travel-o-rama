import os

os.environ["SECRET_KEY"] = "Maja-page"

from os import path
if path.exists("env.py"):
  import env 

SECRET_KEY = os.environ.get('SECRET_KEY')