from flask import Flask, request
import api as _api

app = Flask(__name__)


@app.route('/api', methods=['POST'])
def api():
    try:
        return getattr(_api, request.json['func'])(*request.json['args'], request=request)
    except TypeError as e:
        if 'takes' in e:
            return '', 403


if __name__ == '__main__':
    app.run()
