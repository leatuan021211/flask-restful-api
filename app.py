from lib import create_app
from flask import send_from_directory

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
