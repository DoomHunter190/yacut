# Сервис укорачивания ссылок.

Его назначение — ассоциировать длинную пользовательскую ссылку с короткой,
которую предлагает сам пользователь или предоставляет сервис.

### Возможности

- Генерация коротких ссылок и связь их с исходными длинными ссылками.
- Переадресация на исходный адрес при обращении к коротким ссылкам.
- REST API

### Технологии
[![Python][Python-badge]][Python-url]
[![Flask][Flask-badge]][Flask-url]
[![SQLAlchemy][SQLAlchemy-badge]][SQLAlchemy-url]



## ⚙ Начало Работы

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
В корне проекта создай `.env` файл
```
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=<URI базы данных, по умолчанию "sqlite:///db.sqlite3">
SECRET_KEY=<секретный ключ>
```
Запуск проекта:
```
flask run
```

Автор | Почта
------------- | -------------
[Doomhunter190](https://github.com/DoomHunter190) | <small>[maximportnov9999@gmail.com](maximportnov9999@gmail.com)

[Python-badge]: https://img.shields.io/badge/python%203.9+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54

[Python-url]: https://www.python.org/

[Flask-badge]: https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white

[Flask-url]: https://flask.palletsprojects.com

[SQLAlchemy-badge]: https://img.shields.io/badge/sqlalchemy-fbfbfb?style=for-the-badge

[SQLAlchemy-url]: https://www.sqlalchemy.org/




[Nginx-url]: https://nginx.org
