from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def _get_folders():
    return []


def _get_cards(folder=None):
    return {
        'page_title': 'gallery',
        'page_description': 'gallery description',
        'objects': []
    }


@app.route('/', methods=['GET'])
def homepage():
    return render_template(
        'base.html',
        page_title='Sam\'s pictures',
        page_description=None,
        objects=_get_folders())

    
@app.route('/gallery/<int:id>', methods=['GET'])
def gallery():
    
    details = _get_cards()
	
    return render_template(
        'base.html',
        page_title=details.get('page_title'),
        page_description=details.get('page_description'),
        cards=details.get('objects'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
