from flask import Flask, render_template, flash, redirect, url_for,request
from webapp.forms import LoginForm, RegistrationForm
from webapp.model import db,User



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/user/login')
    def login():
        title="Добро пожаловать в Apotheka"
        login_form=LoginForm()
        return render_template('/user/login.html',title=title,form=login_form)

    @app.route('/user/regisration',methods = ['POST', 'GET'])
    def regisration():
        title="Регистрация в Apotheka"
        login_form = RegistrationForm(request.form) 
        if request.method == 'POST' and login_form.validate():
           #user = User(login_form.username.data, login_form.email.data,
            #           login_form.password.data)
           #db_session.add(user)
           flash('Спасибо за регистрацию')
           return redirect(url_for('login'))
        return render_template('/user/registration.html',title=title,form=login_form)

    @app.route('/user/userProfile',methods = ['POST', 'GET'])
    def userProfile():
        title="Профайл пользователя"
        login_form = RegistrationForm(request.form)
        if request.method == 'POST' and login_form.validate():
           #user = User(login_form.username.data, login_form.email.data,
            #           login_form.password.data)
           #db_session.add(user)
           flash('Ваши данные успешно сохранились')
           return redirect(url_for('login'))
        return render_template('/user/userProfile.html',title=title,form=login_form)
        
    @app.route('/process_login',methods = ['POST'])
    def process_login():
        return "Сейчас проверим!"
        


    return app