from flask import Flask, request, render_template,  redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db,  connect_db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  =  False
app.config['SQLALCHEMY_ECHO'] =  True
app.config['SECRET_KEY'] = "dfdvknerot34iuh4t39hi"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home():
    """redirect to shows list of all users in db"""
    return redirect('/users')

@app.route('/users')
def list_users():
    """Shows list of all users in db"""
    users = User.query.all()
    return render_template('list.html', users=users)

@app.route('/users/new')
def new_user():
    """show form to collect info for a new user"""
    return render_template('add_user.html')

@app.route('/users/new', methods=["POST"])
def add_user():
    """add a new user to db and redirect to users"""
    
    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    image_url = request.form["imageurl"]
    if image_url == "":
        new_user  = User(first_name=first_name, last_name=last_name)
    else:
        new_user  = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect(f'/users')

@app.route("/users/<int:user_id>")
def show_user(user_id):
    """Show details about a user"""
    user = User.query.get_or_404(user_id)
    return render_template("user_details.html", user=user)

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    """show form to update a user's info"""
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/users/<int:user_id>/edit', methods=["POST"])
def edit_user_post(user_id):
    """update a user's info using the form input"""
    user = User.query.get_or_404(user_id)

    first_name = request.form["firstname"]
    last_name = request.form["lastname"]
    image_url = request.form["imageurl"]

    user.first_name = first_name
    user.last_name = last_name
    user.image_url = image_url

    db.session.commit()

    return redirect(f'/users')

@app.route('/users/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """delete a user from db using the id"""
    delete_user  = User.query.filter(User.id == user_id).delete()
    db.session.commit()
    return redirect(f'/users')
