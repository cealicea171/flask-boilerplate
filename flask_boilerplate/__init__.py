from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'YAYYYY YOU FINALLY WORK!'

    return app
