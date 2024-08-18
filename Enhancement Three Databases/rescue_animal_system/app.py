from flask import Flask, render_template
from flask_pymongo import PyMongo
from flask_login import LoginManager, UserMixin
from routes import register_routes, intake_routes, profile_routes, login_routes, animal_routes, print_routes

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/rescueAnimalDB"
app.config['SECRET_KEY'] = 'your_secret_key'

mongo = PyMongo(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin):
    def __init__(self, id, username, password, email=None, first_name=None, last_name=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name

@login_manager.user_loader
def load_user(user_id):
    user_data = mongo.db.users.find_one({"id": user_id})
    if user_data:
        email = user_data.get('email', 'no_email@example.com')
        first_name = user_data.get('first_name', 'NoFirstName')
        last_name = user_data.get('last_name', 'NoLastName')
        return User(user_data['id'], user_data['username'], user_data['password'], email, first_name, last_name)
    return None

@app.route('/')
def index():
    return render_template('index.html')

# Register the routes
register_routes(app)
intake_routes(app)
profile_routes(app)
login_routes(app)
animal_routes(app)
print_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
