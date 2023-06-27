from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo

from flask_wtf.file import FileField, FileAllowed,FileRequired


class SignupForm(FlaskForm):
    fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
   
    email = StringField("Your Email",validators=[Email()])
    password = PasswordField("Password",validators=[DataRequired()])
    confirm_password= PasswordField("Confirm password",validators =[EqualTo('password',message="Confirm password must be equal to password")])
   # message = TextAreaField("Message", validators=[Length(1,3)])
    
    btn = SubmitField("Sign Up!")
 


class ProfileForm(FlaskForm):
     fullname = StringField("Fullname",validators=[DataRequired(message="your fullname is required")])
     pix =FileField("Display picture", validators=[FileRequired(), FileAllowed(["jpg","png"], "Image only!")])
     btn=SubmitField("update profile!")
     
  
    
    
    
    
    
     
    

