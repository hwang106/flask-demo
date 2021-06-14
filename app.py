# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
# allows us to send html file as one hard-coded unit
from flask import render_template
#allows us to access form data
from flask import request, redirect
from model import get_breakfast_rating
from datetime import datetime


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time=datetime.now())
    #don't need path since render_template method always looks for the file in the templates folder by default

@app.route('/secret')
def secret():
    return "You found the secret page!"
# Had to add methods parameter and include POST (GET is default) so that post method is allowed.
@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        print(request.form["breakfast"])
        user_breakfast = request.form["breakfast"]
        user_nickname = request.form["nickname"]
        breakfast_rating = get_breakfast_rating(user_breakfast)
        return render_template("results.html", bleh=user_breakfast, meh=user_nickname, rating=breakfast_rating)
    else:
        return redirect('/')
