from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import InputRequired, Email, EqualTo, ValidationError, Length


# Login Class
class LoginForm(FlaskForm):
    ''' Login validation form field'''
    email = StringField('Email', validators=[InputRequired(), Email(message="Email should have an @")])
    password = PasswordField('Password', validators=[InputRequired(), Length(6,20, message="Password must be 6 to 20 characters long!!!")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


# Login Class
class RegistrationForm(FlaskForm):
    ''' Registration validation form field'''
    username = StringField('Username', validators=[InputRequired(), Length(6,20, message="Username must be 6 to 20 characters long!!!")])
    email = StringField('Email', validators=[InputRequired(), Email(message="Email should have an @")])
    password = PasswordField('Password', validators=[InputRequired(), Length(6,20, message="Password must be 6 to 20 characters long!!!")])
    confirm_password = PasswordField('Repeat Password', validators=[
        InputRequired(), EqualTo('password', message="Password Must Match!")])
    submit = SubmitField('Register')
