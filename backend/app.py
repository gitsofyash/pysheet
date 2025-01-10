from flask import Flask
from routes import routes  # Import the routes Blueprint

app = Flask(__name__)
app.register_blueprint(routes)  # Register the Blueprint

if __name__ == '__main__':
    app.run(debug=True)
