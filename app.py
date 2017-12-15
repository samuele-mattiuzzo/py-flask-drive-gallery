from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


HOMEPAGE_FOLDER = '1ZHuzg4-UzaT9ewBC_W_hwnsSc4CsisfC'
HOMEPAGE = {
    'page_title': 'Sam\'s gallery',
    'page_description': 'A recollection of my best moments while travelling'
}
PICTURE_FOLDERS = {
    '1vbEp_630b80gSYIkRh-JlJg_lka4UOWV': {
        'page_title':'Altea, Costa Blanca',
        'date': 'February 2017'
    },
    '1INuY3P6WA8LSC0Ejx4ofCaEv3wFogw4j': {
        'page_title': 'Portland, Dorset',
        'date': 'June 2017'
    },
    '1INuY3P6WA8LSC0Ejx4ofCaEv3wFogw4j': {
        'page_title': 'Portland, Dorset',
        'date': 'September 2017'
    },
    '1W2wqbMghtSNRcgz020L9e_hCwJcq4x-r': {
        'page_title': 'Altea, Costa Blanca',
        'date': 'October 2017'
    },
    '1P0PwMXAqPZBFfF_Mc53w6QSZJvbZypb9': {
        'page_title': 'Hay-on-Wye, Wales',
        'date': 'December 2017'
    },
}


def _get_cards(folder=None):
    if folder:
        return PICTURE_FOLDERS[folder]
    else:
        return HOMEPAGE
        

@app.route('/', methods=['GET'])
def homepage():
    
    details = _get_cards()
    
    return render_template(
        'base.html',
        page_title=details.get('page_title'),
        page_description=details.get('page_description'),
        objects=PICTURE_FOLDERS
    )

    
@app.route('/gallery/<string:folder_id>', methods=['GET'])
def gallery(folder_id):
    
    details = _get_cards(folder_id)
	
    return render_template(
        'base.html',
        page_title=details.get('page_title'),
        page_description=details.get('date'),
        folder_id=folder_id,
        cta=True
    )


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
