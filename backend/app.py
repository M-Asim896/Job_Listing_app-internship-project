from flask import Flask
from flask_cors import CORS
from config import SQLALCHEMY_DATABASE_URI
from models import db
from routes import routes

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})   # ✅ Allow all origins

app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
app.register_blueprint(routes)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0')  # ✅ Enables access from localhost too
