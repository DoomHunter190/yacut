from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from settings import MAX_SHORT_ID_SIZE, MAX_URL_SIZE


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    URL(message='Введите корректный URL адрес'),
                    Length(max=MAX_URL_SIZE)]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(max=MAX_SHORT_ID_SIZE),
                    Optional(), Regexp(
                        r'^[A-Za-z0-9]+$',
                        message='Можно использовать только [A-Za-z0-9]')]
    )
    submit = SubmitField('Создать')