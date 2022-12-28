from flask_app import app
from flask import render_template,redirect,request, flash, session
from flask_app.models.game import Game
import random
# from flask_app.models.user import User

@app.route('/')
def begin():
    if 'page_number' not in session:
        session['page_number'] = 0
    return render_template("index.html")

@app.route('/startgame')
def startitup():
    session['start'] = "Started"
    return redirect('/')

@app.route('/getname', methods=['POST'])
def getname():
    session['name'] = request.form['name']
    return redirect('/')

@app.route('/chooseShirt', methods=['POST'])
def chooseShirt():
    session['shirt'] = request.form['shirt']
    willRedShirtDie = ["Yes", "No"]
    session['will_red_shirt_die'] = random.choice(willRedShirtDie)
    return redirect('/')

@app.route('/explore', methods=['POST'])
def chooseExplore():
    session['explore'] = request.form['explore']
    return redirect('/')

@app.route('/getlocation', methods=['POST'])
def getlocation():
    session['location'] = request.form['location']
    return redirect('/')

@app.route('/getencounter', methods=['POST'])
def getencounter():
    session['encounter'] = request.form['encounter']
    return redirect('/')

@app.route('/nextpage')
def next():
    session['page_number'] += 1
    return redirect('/')

@app.route('/friendly')
def isfriendly():
    session['friendly'] = random.randint(0, 1)
    session['page_number'] += 1
    return redirect('/')

@app.route('/restart')
def clear():
    if 'uid' in session:
        temp = session['uid']
        session.clear()
        session['uid'] = temp
    else:
        session.clear()
    return redirect('/')

@app.route('/save')
def savegame():
    data = {
        "shirt" : "",
        "page_number" : 0,
        "name" : "",
        "explore" : "",
        "location" : "",
        "encounter" : "",
        "friendly" : 2,
        "user_id" : session['uid']
    }
    for key in session:
        data[key] = session[key]
    if 'gid' in session:
        data['id'] = session['gid']
        Game.updategame(data)
    else:
        session['gid'] = Game.save(data)
    return redirect('/')

@app.route('/open/<int:id>')
def opengame(id):
    if 'uid' in session:
        temp = session['uid']
    session.clear()
    session['uid'] = temp
    game = Game.getbyid(id)
    for attr, value in vars(game).items():
        if value != "":
            session[attr] = value
    session['gid'] = id
    if session['shirt'] == "Red Shirt":
        willRedShirtDie = ["Yes", "No"]
        session['will_red_shirt_die'] = random.choice(willRedShirtDie)
    session['start'] = "Started"
    return redirect('/')

@app.route('/credits')
def credits():
    return render_template("credits.html")