# FLASK-TASK-MANAGER — менеджер задач с авторизацией
Простое веб-приложение на Flask для управления задачами. Поддерживает регистрацию, вход в систему и добавление задач. Пользователи видят только свои задачи.

## 🧰 Стек технологий

### 🔧 Backend
[![Flask](https://img.shields.io/badge/Flask-2.3+-blue?logo=flask)](https://flask.palletsprojects.com/)
[![Jinja2](https://img.shields.io/badge/Jinja2-3.1+-orange?logo=jinja)](https://jinja.palletsprojects.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?logo=sqlalchemy)](https://www.sqlalchemy.org/)
[![Flask-Login](https://img.shields.io/badge/Flask--Login-auth-green)](https://flask-login.readthedocs.io/)
[![WTForms](https://img.shields.io/badge/WTForms-3.1+-lightgrey)](https://wtforms.readthedocs.io/)
[![Flask-WTF](https://img.shields.io/badge/Flask--WTF-1.2+-yellow)](https://flask-wtf.readthedocs.io/)

### 💅 Frontend
[![Bootstrap](https://img.shields.io/badge/Bootstrap_5-CSS_Framework-purple?logo=bootstrap)](https://getbootstrap.com/)

### 🐳 Контейнеризация

[![Docker](https://img.shields.io/badge/Docker-container-blue?logo=docker)](https://www.docker.com/)
[![docker-compose](https://img.shields.io/badge/docker--compose-setup-informational?logo=docker)](https://docs.docker.com/compose/)

### 🧹 Качество кода
[![pre-commit](https://img.shields.io/badge/pre--commit-hooks-yellowgreen?logo=pre-commit)](https://pre-commit.com/)
[![ruff](https://img.shields.io/badge/Ruff-linter-green?logo=python)](https://docs.astral.sh/ruff/)

### 🧪 Тестирование
[![pytest](https://img.shields.io/badge/pytest-testing-yellow?logo=pytest)](https://docs.pytest.org/)

### ⚙️ CI/CD
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI/CD-blue?logo=githubactions)](https://github.com/features/actions)

## Как запустить
1. Клонируем репозиторий (via SSH):
```bash
git clone git@github.com:MrFR0D0/FLASK-TASK-MANAGER.git
```
2. Создаем и активируем виртуальное окружение
для 💻 macOS / 🐧 Linux
```bash
python3 -m venv venv
source venv/bin/activate
```
для 🖥 Windows
```bash
python -m venv venv
venv\Scripts\activate
```
3. Обновляем pip и устанавливаем необходимые зависимости из requirements.txt
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
4. Переменные окружения
Добавляем .env (пример заполнения в .env.example).
5. Запускаем приложение (из корня проекта)
```bash
python3 run.py
```
6. Работа с приложением
Запущенное приложение доступно по адресу
[http://127.0.0.1:5000](http://127.0.0.1:5000)

## Разработка в команде
1. Для поддержания единообразиция кода, необходимо выполнить установку хуков pre-commit. Этот инструмент не позволит выполнить commit с нарушением оформления кода.
Находясь в корне проекта необходимо выполнить команду
```bash
pre-commit install
```
