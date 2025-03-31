from flask import Flask
from flask_cors import CORS
from routes import search_bp

app = Flask(__name__)
CORS(app, resources={r"/search": {"origins": "http://localhost:8080"}})


app.register_blueprint(search_bp)

if __name__ == '__main__':
    app.run(debug=True)
