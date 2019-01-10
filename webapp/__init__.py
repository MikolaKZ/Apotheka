from flask import Flask, render_template, flash, redirect, url_for
from webapp.forms import LoginForm
from webapp.model import db,User



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    db.init_app(app)
    @app.route('/')
    def index():
        return redirect(url_for('login'))

    @app.route('/login')
    def login():
        title="Добро пожаловать в Apotheka"
        login_form=LoginForm()
        return render_template('login.html',title=title,form=login_form)

    @app.route('/regisration')
    def regisration():
        return "Да начнется регистрация!"
        
    @app.route('/process_login')
    def process_login():
        return "Сейчас проверим!"


    return app
