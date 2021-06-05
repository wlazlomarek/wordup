from flask import Flask, render_template
from google_sheet import read_google_sheet
import random

app = Flask(__name__, template_folder='www/templates',
            static_folder='www/static')

vocabulary = None
word_amount = 5


@app.route('/all')
def json_voc():
    voc = vocabulary or update_from_google()
    return voc


@app.route('/update_db', methods=['GET', 'POST'])
def update_from_google():
    global vocabulary
    vocabulary = read_google_sheet()
    print('[info] Database has been updated by user')
    return {'counter': len(vocabulary),
            'status': 'success'}, 200


@app.route('/', methods=['GET', 'POST'])
def main():
    update_from_google()
    vb = dict()
    while len(vb) < word_amount:
        k = random.choice(list(vocabulary.keys()))
        vb[k] = vocabulary[k]
    return render_template('index.html', vocabulary=vb), 200


if __name__ == "__main__":
    app.run()
