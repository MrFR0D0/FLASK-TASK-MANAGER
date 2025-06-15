from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required

from . import db
from .models import Task

main = Blueprint("main", __name__)


@main.route("/")
@login_required
def index():
    """Обработчик главной страницы."""
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", tasks=tasks)


@main.route("/add", methods=["POST"])
@login_required
def add():
    """Обработчик страницы добавления задачи."""
    title = request.form.get("title")
    if title:
        task = Task(title=title, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for("main.index"))
