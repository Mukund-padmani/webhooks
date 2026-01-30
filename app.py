from flask import Flask
from routes import webhook_bp

app = Flask(__name__)

app.register_blueprint(webhook_bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000, use_reloader=False)

