from http import HTTPStatus

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .error_handlers import GenerationError
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    original, short = form.original_link.data, form.custom_id.data
    if URLMap.get_url_map(short):
        flash('Предложенный вариант короткой ссылки уже существует.')
        return render_template('index.html', form=form)
    if (short != '' and
       short is not None and
       not URLMap.short_id_is_correct(short)):
        flash('Указано недопустимое имя для короткой ссылки')
        return render_template('index.html', form=form)
    try:
        url_map = URLMap.create_url_map(original, short)
        db.session.add(url_map)
        db.session.commit()
    except GenerationError:
        abort(HTTPStatus.INTERNAL_SERVER_ERROR)
    return render_template(
        'index.html',
        form=form,
        result_url=url_for('index_view', _external=True) + url_map.short
    )


@app.route('/<short_id>', methods=['GET'])
def redirect_view(short_id):
    url_map = URLMap.get_url_map(short_id)
    if url_map:
        return redirect(url_map.original)
    abort(HTTPStatus.NOT_FOUND)