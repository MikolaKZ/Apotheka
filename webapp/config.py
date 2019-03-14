import os
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "sdafsadfqw!@#!F,dfasasdfas25479"
YA_MAP_KEY = "341f9917-3701-49b3-b946-63708ed47a04"

REMEMBER_COOKIE_DURATION = timedelta(days=5)
# Работа с изображениями
UPLOAD_FOLDER = os.path.join(basedir, 'photos')
UPLOADED_FILES_ALLOW = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024
