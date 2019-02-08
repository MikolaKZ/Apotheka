import os
from datetime import timedelta

## os
basedir=os.path.abspath(os.path.dirname(__file__))
## webapp
SECRET_KEY="sdafsadfqw!@#!F,dfasasdfas25479"
REMEMBER_COOKIE_DURATION= timedelta(days=5)
## Работа с изображениями
UPLOAD_FOLDER=os.path.join(basedir,'photos')
UPLOADED_FILES_ALLOW=set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH =16 * 1024 * 1024
## sqlalchemy db
SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(basedir,'..','webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False