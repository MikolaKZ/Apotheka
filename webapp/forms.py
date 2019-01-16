from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, PasswordField, validators,SubmitField,DecimalField

class LoginForm(FlaskForm):
    username=StringField('Имя пользователя', validators=[validators.DataRequired()],render_kw={"class":"form-control", "placeholder":"Имя пользователя"})
    password=PasswordField('Пароль',validators=[validators.DataRequired()],render_kw={"class":"form-control", "placeholder":"Пароль" })
    submit=SubmitField("Войти",render_kw={"class":"btn btn-lg btn-primary btn-block" })
    remember_me=BooleanField("Запомни меня",default=True, render_kw={"class":"form-check-input", "type":"checkbox", "id":"gridCheck" })
    

class RegistrationForm(FlaskForm):
    age = DecimalField('Возвраст', [ validators.NumberRange(3, 200, message="Укажите свой возвраст от 3 до 200 лет")],render_kw={"class":"form-control", "placeholder":"18"})
    email = StringField('Email', [ validators.DataRequired(),validators.Email(message="Email введен неверно")],render_kw={"class":"form-control" ,"placeholder":"твой@емэйл.где"})
    password = PasswordField('Новый пароль', [
        validators.DataRequired(message='Введите пароль'),validators.Length(min=8, max=25, message='Пароль должен состоять как минимум из 8 символов'),
        validators.EqualTo('confirm', message='Пароли должны совпадать')
    ],render_kw={"class":"form-control"})
    confirm = PasswordField('Повторите пароль',render_kw={"class":"form-control"})
    Name=StringField('Имя', [validators.DataRequired(message="Введите Имя")],render_kw={"class":"form-control", "placeholder":"Иван"})
    Sername=StringField('Фамилия', [validators.DataRequired(message="Введите Фамилию")],render_kw={"class":"form-control", "placeholder":"Федоров"})
     # isWoman=
    user_name=StringField('Псевдоним', [validators.Length(min=3, max=25, message="Псевдоним должен быть более 4 символов")],render_kw={"class":"form-control", "placeholder":"Псевдоним"})
    submit=SubmitField("Продолжить",render_kw={"class":"btn btn-primary btn-lg btn-block" })
    

