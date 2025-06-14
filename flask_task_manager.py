import os

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
from flask_login import (
    LoginManager,
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from werkzeug.security import check_password_hash, generate_password_hash
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, ValidationError

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"


# Models
class User(db.Model, UserMixin):
    """Модель пользователя."""

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


class Task(db.Model):
    """Модель задачи."""

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# Forms
class RegisterForm(FlaskForm):
    """Форма регистрации пользователя."""

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


# Login Manager
@login_manager.user_loader
def load_user(user_id):
    """Получение пользователя."""
    return User.query.get(int(user_id))


# Routes
@app.route("/")
@login_required
def index():
    """Обработчик Главной страницы."""
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", tasks=tasks)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Обработчик страницы регистрации."""
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        user = User(username=form.username.data, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful!", "success")
        return redirect(url_for("login"))
    return render_template("register.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Обработчик страницы логина."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("index"))
        flash("Invalid username or password.", "danger")
    return render_template("login.html", form=form)


@app.route("/logout")
@login_required
def logout():
    """Обработчик страницы логаута."""
    logout_user()
    return redirect(url_for("login"))


@app.route("/add", methods=["POST"])
@login_required
def add():
    """Обработчик страницы добавления задачи."""
    title = request.form.get("title")
    if title:
        task = Task(title=title, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
