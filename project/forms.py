from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Username is required.')], render_kw={'class': 'form-control'},
                id = 'username', name = 'username')
    password = PasswordField('Password', validators=[DataRequired(message='Password is required.')], render_kw={'class': 'form-control'},
                id = 'password', name = 'password')
    submit = SubmitField('Sign In', render_kw={'class': 'btn btn-primary'},
                id = 'submit', name = 'submit')