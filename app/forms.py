from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

from .models import User


class RegisterForm(FlaskForm):
    """Форма регистрации."""

    username = StringField(
        "Username", validators=[DataRequired(), Length(min=3)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6)]
    )
    confirm = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")

    def validate_username(self, username):
        """Проверка уникальности имени пользователя."""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("Username already exists.")


class LoginForm(FlaskForm):
    """Форма логина."""

    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")
