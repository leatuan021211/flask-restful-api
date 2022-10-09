from lib import create_app
from flask import send_from_directory

if __name__ == "__main__":
    app = create_app()
    @app.route('/static/<path:path>')
    def send_static(path):
        return send_from_directory('static', path)
    app.run(debug=True)