from flask_wtf import FlaskForm
from .models import User
from wtforms import StringField, PasswordField, SubmitField,BooleanField
from wtforms.validators import DataRequired, EqualTo, Email, ValidationError

class UserForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Shipping Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    def validate_username(self,username):
        user = user.query.filter_by(username=username.data).first()
        if user is not None: 
            raise ValidationError('This username is not available, please re-check your credentials and try again.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('It looks like an account already exists with this email address.')

class UserUpdateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address = StringField('Shipping Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    zip = StringField('Zip Code', validators=[DataRequired()])
    submit = SubmitField('Submit')
    
    def __init__(self, original_username, original_email, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email
        
    def validate_username(self, username):
        print('test user')
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('This username is not available, please re-check your credentials and try again.')                
                
    def validate_email(self, email):
        print("test email")
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('It looks like an account already exists with this email address.')
                
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ResetPasswordRequestForm(Flaskform):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Reset Password')
    
class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    passwordII = PasswordField('Confirm your Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')