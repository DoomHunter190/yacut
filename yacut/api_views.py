from http import HTTPStatus

from flask import jsonify, request, url_for

from . import app, db
from .error_handlers import GenerationError, InvalidAPIUsage
from .models import URLMap


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_url(short_id):
    url_map = URLMap.get_url_map(short_id)
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    if not URLMap.short_id_is_correct(short_id):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки')
    return jsonify({'url': url_map.original}), HTTPStatus.OK


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    original, short = data['url'], None
    if not URLMap.url_is_correct(original):
        raise InvalidAPIUsage(
            'Введите корректный URL адрес')
    if ('custom_id' in data and
       data['custom_id'] is not None and
       data['custom_id'] != ''):
        short = data['custom_id']
        if not URLMap.short_id_is_correct(short):
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки')
        if URLMap.get_url_map(short):
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.')
    try:
        url_map = URLMap.create_url_map(original, short)
        db.session.add(url_map)
        db.session.commit()
    except GenerationError as error:
        return error.to_dict(), error.status_code
    return jsonify({
        'url': url_map.original,
        'short_link': url_for('index_view', _external=True) + url_map.short
    }), HTTPStatus.CREATED