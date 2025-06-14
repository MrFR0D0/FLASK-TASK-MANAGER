В шаблоне имеется настрока для линтера и форматтера Ruff + pre-commit

# Использование pre-commti
## 📦 Установка

### Установка через pip

```bash
pip install pre-commit
```

### Пример настройки необходимых хуков в ".pre-commit-config.yaml"

```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.11.13
  hooks:
    - id: ruff-check
      name: ruff check
      description: "Run 'ruff check' for extremely fast Python linting"
      entry: ruff check --force-exclude
      language: python
      types_or: [python, pyi, jupyter]
      args: [--fix, --exit-non-zero-on-fix]
      require_serial: true
      additional_dependencies: []
      minimum_pre_commit_version: "2.9.2"
    - id: ruff-format
      name: ruff format
      description: "Run 'ruff format' for extremely fast Python formatting"
      entry: ruff format --force-exclude
      language: python
      types_or: [python, pyi, jupyter]
      args: [--exit-non-zero-on-fix]
      require_serial: true
      additional_dependencies: []
      minimum_pre_commit_version: "2.9.2"
```
### Включение хуков в Python
```bash
pre-commit install
```
После этого, любой
 ```bash
 git commit
 ```
 будет сопровождаться выполнением всех хуков, описанных в ".pre-commit-config.yaml"
 
# Использование Ruff для проверки и форматирования Python-кода

[Ruff](https://github.com/astral-sh/ruff) — это быстрый и мощный инструмент для статического анализа Python-кода, сочетающий в себе функции линтера, форматтера и автофиксатора ошибок. Ruff написан на Rust и поддерживает множество популярных правил, включая flake8, isort, pycodestyle и другие. Официальную документацию можно посмотреть [тут](https://docs.astral.sh/ruff/).

## 📦 Установка

### Установка через pip

```bash
pip install ruff
```
### Установка через Homebrew (macOS/Linux)
```bash
brew install ruff
```
### Проверка установки
```bash
ruff --version
```

## ⚙️ Настройка конфигурации
Создайте файл pyproject.toml (или используйте ruff.toml) в корне проекта:
```toml
[tool.ruff]
line-length = 88
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "D", "UP", "Q", "TCH", "PD", "NPY", "RUF"]
ignore = ["D100", "D104"]

[tool.ruff.format]
quote-style = "single"
indent-style = "space"
line-ending = "lf"

[tool.ruff.lint.pydocstyle]
convention = "google"
```
### Часто используемые настройки
* line-length: максимальная длина строки (по умолчанию 88);
* target-version: версия Python (например, "py39", "py310");
* select: включаемые категории ошибок (см. документацию Ruff);
* ignore: игнорируемые категории ошибок.

## 🧹 Использование Ruff
### Анализ кода
```bash
ruff check .
```
### Автоматическое исправление
```bash
ruff check --fix .
```
### Форматирование кода
```bash
ruff format .
```
