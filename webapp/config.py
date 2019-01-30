import os
from datetime import timedelta

basedir=os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI="sqlite:///"+os.path.join(basedir,'..','webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY="sdafsadfqw!@#!F,dfasasdfas25479"

REMEMBER_COOKIE_DURATION= timedelta(days=5)
## Работа с изображениями
UPLOAD_FOLDER=os.path.join(basedir,'photos')
#TODO Если этим UPLOADED DEST не пользуются, надо его убрать
UPLOADED_FILES_DEST="/user_pictures"
UPLOADED_FILES_ALLOW=set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH =16 * 1024 * 1024


