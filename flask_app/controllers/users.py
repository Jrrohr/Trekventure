from flask_app import app, bcrypt
from flask import render_template,redirect,request, flash, session
from flask_app.models.user import User
from flask_app.models.game import Game

@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        flash("Not logged in!", 'login')
        return redirect('/')
    user = User.find_by_id(session['uid'])
    games = Game.get_all(session['uid'])
    return render_template("dashboard.html", user=user, games=games)

@app.route('/register', methods=['POST'])
def create():
    if not User.validate(request.form):
        return redirect('/')
    hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        "password" : hash
    }
    user = User.register(data)
    session['uid'] = user
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    logged_in = User.validate_login(request.form)
    if not logged_in:
        return redirect('/')
    session['uid'] = logged_in.id
    return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')