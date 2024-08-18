from flask import request, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from models import Animal, User
from forms import AnimalForm, RegistrationForm, ProfileForm
import bcrypt
import uuid
from bson.objectid import ObjectId

def register_routes(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegistrationForm()
        if request.method == 'POST' and form.validate_on_submit():
            existing_user = mongo.db.users.find_one({"username": form.username.data})
            if existing_user is None:
                # Hash the password and create a new user
                hashed_password = bcrypt.hashpw(form.password.data.encode('utf-8'), bcrypt.gensalt())
                user = {
                    "id": str(uuid.uuid4()),
                    "username": form.username.data,
                    "password": hashed_password,
                    "email": form.email.data,
                    "first_name": form.first_name.data,
                    "last_name": form.last_name.data
                }
                mongo.db.users.insert_one(user)
                flash('Registration successful. Please log in.')
                return redirect(url_for('login'))
            flash('Username already exists.')
        return render_template('register.html', form=form)

def intake_routes(app):
    @app.route('/intake_options')
    @login_required
    def intake_options():
        return render_template('intake_options.html')

    @app.route('/intake/<animal_type>', methods=['GET', 'POST'])
    @login_required
    def intake_animal(animal_type):
        form = AnimalForm()
        if request.method == 'POST' and form.validate_on_submit():
            # Create a new animal and insert into the database
            animal = Animal(
                name=form.name.data,
                animal_type=animal_type,
                gender=form.gender.data,
                age=form.age.data,
                weight=form.weight.data,
                acquisition_date=form.acquisition_date.data,
                acquisition_country=form.acquisition_country.data,
                training_status=form.training_status.data,
                reserved=form.reserved.data,
                in_service_country=form.in_service_country.data
            )
            mongo.db.animals.insert_one(animal.to_dict())
            return redirect(url_for('index'))
        return render_template('intake_form.html', animal_type=animal_type, form=form)

def profile_routes(app):
    @app.route('/profile', methods=['GET', 'POST'])
    @login_required
    def profile():
        form = ProfileForm(request.form, obj=current_user)
        if request.method == 'POST' and form.validate():
            # Update user profile in the database
            mongo.db.users.update_one(
                {"id": current_user.id},
                {"$set": {
                    "email": form.email.data,
                    "first_name": form.first_name.data,
                    "last_name": form.last_name.data
                }}
            )
            flash('Profile updated successfully.')
            return redirect(url_for('profile'))
        return render_template('profile.html', form=form)

def login_routes(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user_data = mongo.db.users.find_one({"username": username})
            if user_data:
                email = user_data.get('email', 'no_email@example.com')
                first_name = user_data.get('first_name', 'NoFirstName')
                last_name = user_data.get('last_name', 'NoLastName')
                # Check the hashed password
                if bcrypt.checkpw(password.encode('utf-8'), user_data['password']):
                    user = User(user_data['id'], user_data['username'], user_data['password'], email, first_name, last_name)
                    login_user(user)
                    return redirect(url_for('index'))
                else:
                    flash('Invalid password')
            else:
                flash('Username not found')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))

def animal_routes(app):
    @app.route('/reserve', methods=['GET', 'POST'])
    @login_required
    def reserve_animal():
        if request.method == 'POST':
            animal_name = request.form['animal_name']
            animal = mongo.db.animals.find_one({"name": animal_name})
            if animal:
                mongo.db.animals.update_one({"name": animal_name}, {"$set": {"reserved": True}})
                return f"<p>Animal {animal_name} reserved successfully</p><a href='{url_for('index')}'>Back to main menu</a>"
            return f"<p>Animal {animal_name} not found</p><a href='{url_for('index')}'>Back to main menu</a>"
        animals = mongo.db.animals.find({"reserved": False})
        animals_list = list(animals)
        return render_template('reserve.html', animals=animals_list)

    @app.route('/edit/<animal_id>', methods=['GET', 'POST'])
    @login_required
    def edit_animal(animal_id):
        animal = mongo.db.animals.find_one({"_id": ObjectId(animal_id)})
        form = AnimalForm(request.form, data=animal)
        if request.method == 'POST' and form.validate_on_submit():
            # Update animal details in the database
            updated_animal = {
                "name": form.name.data,
                "animal_type": animal['animal_type'],
                "gender": form.gender.data,
                "age": form.age.data,
                "weight": form.weight.data,
                "acquisition_date": form.acquisition_date.data,
                "acquisition_country": form.acquisition_country.data,
                "training_status": form.training_status.data,
                "reserved": form.reserved.data,
                "in_service_country": form.in_service_country.data
            }
            mongo.db.animals.update_one({"_id": ObjectId(animal_id)}, {"$set": updated_animal})
            return redirect(url_for('reserve_animal'))
        return render_template('edit_form.html', form=form)

    @app.route('/delete/<animal_id>', methods=['POST'])
    @login_required
    def delete_animal(animal_id):
        mongo.db.animals.delete_one({"_id": ObjectId(animal_id)})
        return redirect(url_for('reserve_animal'))

    def quicksort_animals(animals, key):
        # Quick sort implementation for sorting animals
        if len(animals) <= 1:
            return animals
        pivot = animals[len(animals) // 2]
        left = [x for x in animals if (float(x[key]) if key == 'age' else x[key]) < (float(pivot[key]) if key == 'age' else pivot[key])]
        middle = [x for x in animals if (float(x[key]) if key == 'age' else x[key]) == (float(pivot[key]) if key == 'age' else pivot[key])]
        right = [x for x in animals if (float(x[key]) if key == 'age' else x[key]) > (float(pivot[key]) if key == 'age' else pivot[key])]
        return quicksort_animals(left, key) + middle + quicksort_animals(right, key)

    @app.route('/print/<animal_type>', methods=['GET'])
    @login_required
    def print_animal_list(animal_type):
        sort_by = request.args.get('sort_by', 'name')
        animals = list(mongo.db.animals.find({"animal_type": animal_type}))
        animals = quicksort_animals(animals, sort_by)
        return render_template('print_list.html', title=f"{animal_type.capitalize()} Details", animals=animals, sort_by=sort_by)

    @app.route('/print_available')
    @login_required
    def print_available_animals():
        sort_by = request.args.get('sort_by', 'name')
        animals = list(mongo.db.animals.find({"reserved": False}))
        animals = quicksort_animals(animals, sort_by)
        return render_template('print_list.html', title="Available Animals", animals=animals, sort_by=sort_by)

    @app.route('/print_all')
    @login_required
    def print_all_animals():
        sort_by = request.args.get('sort_by', 'name')
        animals = list(mongo.db.animals.find())
        animals = quicksort_animals(animals, sort_by)
        return render_template('print_list.html', title="All Animals", animals=animals, sort_by=sort_by)

    @app.route('/search', methods=['GET'])
    @login_required
    def search():
        query = request.args.get('query')
        animals = list(mongo.db.animals.find({"name": {"$regex": query, "$options": "i"}}))
        return render_template('search_results.html', query=query, animals=animals)

def print_routes(app):
    @app.route('/print_options')
    @login_required
    def print_options():
        return render_template('print_options.html')
