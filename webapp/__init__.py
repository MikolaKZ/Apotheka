import os
import os.path
from flask_migrate import Migrate
from webapp.model import db, User, Profile
from webapp.otherFunc import str_to_bool
from werkzeug.utils import secure_filename
from werkzeug import SharedDataMiddleware
from sqlalchemy.exc import IntegrityError
from webapp.forms import (LoginForm, RegistrationForm, PhotoForm,
                          RegistrationFormWithoutPassword)
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask import (Flask, render_template, flash, redirect, url_for, request,
                   send_from_directory)


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "login"
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('main'))
        return redirect(url_for('login'))

    @app.route('/content/main')
    def main():
        title = "Apotheka"
        return render_template('/content/main.html', title=title)

    @app.route('/user/login')
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('main'))
        title = "Добро пожаловать в Apotheka"
        login_form = LoginForm()
        return render_template('/user/login.html', title=title,
                               form=login_form)

    @app.route('/user/regisration', methods=['POST', 'GET'])
    def regisration():
        title = "Регистрация в Apotheka"
        login_form = RegistrationForm(request.form)
        if request.method == 'POST' and login_form.validate():
            user = User(username=login_form.user_name.data,
                        email=login_form.email.data,
                        userTelegrammChat=request.form.get("telegram"))
            try:
                user.set_password(login_form.password.data)
                db.session.add(user)
                db.session.commit()
                profile = Profile(user_id=user.id,
                                  name=login_form.Name.data,
                                  sername=login_form.Sername.data,
                                  age=int(login_form.age.data),
                                  isWoman=(
                                    # Не уверен на счет верности переноса
                                    str_to_bool(request.form.get("gender"))))
                db.session.add(profile)
                db.session.commit()
                flash('Спасибо за регистрацию')
                return redirect(url_for('login'))
            except IntegrityError:
                flash('Пользователи с такими данными уже существуют')
                return redirect(url_for('regisration'))
        return render_template('/user/registration.html',
                               title=title, form=login_form,
                               User="", Profile="")

    @app.route('/user/userProfile', methods=['POST', 'GET'])
    @login_required
    def userProfile():
        title = "Профайл пользователя"
        login_form = RegistrationFormWithoutPassword(request.form)
        photoForm = PhotoForm(request.form)

        if request.method == 'POST' and login_form.validate():
            profile = Profile.query.filter_by(user_id=(
                                              current_user.get_id()).first())
            user = User.query.filter_by(id=current_user.get_id()).first()
            user.username = login_form.user_name.data
            user.email = login_form.email.data
            user.userTelegrammChat = request.form.get("telegram")
            db.session.commit()
            profile.name = login_form.Name.data
            profile.country = request.form.get("country")
            profile.city = request.form.get("city")
            profile.sername = login_form.Sername.data
            profile.age = int(login_form.age.data)
            profile.isWoman = str_to_bool(request.form.get("gender"))
            db.session.commit()
            flash('Данные успешно перезаписаны')
            return redirect(url_for('login'))

        profile = Profile.query.filter_by(user_id=(
                                            current_user.get_id()).first())
        user = User.query.filter_by(id=current_user.get_id()).first()
        return render_template('/user/userProfile.html', title=title,
                               form=login_form, photoForm=photoForm, User=user,
                               Profile=profile)

    @app.route('/process_login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user, remember=form.remember_me.data)
                flash("Вы успешно зашли на сайт")
                return redirect(url_for('userProfile'))
            flash("Неправильное имя и пароль")
            return redirect(url_for('login'))

    @app.route('/uploads', methods=['GET', 'POST'])
    def upload():
        form = PhotoForm()
        if form.validate_on_submit():
            f = form.photo.data
            filename = secure_filename(f.filename)
            file_obj = filename[-3:]
            filename = 'avatar.'+file_obj
            avatar_path = os.path.join(app.config["UPLOAD_FOLDER"],
                                       current_user.get_id(), filename)
            try:
                f.save(avatar_path)
            except (FileNotFoundError):
                os.makedirs(os.path.join(app.config["UPLOAD_FOLDER"],
                                         current_user.get_id()))
                f.save(avatar_path)
            profile = Profile.query.filter_by(user_id=(
                                                current_user.get_id()).first())
            profile.Avatar = avatar_path
            db.session.commit()
        return redirect(url_for('userProfile'))

    @app.route('/uploads/<filename>')
    def uploaded_image(filename):
        return send_from_directory(os.path.join(app.config['UPLOAD_FOLDER'],
                                   current_user.get_id()), filename)
    return app
