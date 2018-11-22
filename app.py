from flask import Flask, request, redirect, url_for
from flask import render_template
from database import get_all_cats, get_cat_id, create_cat, add_vote

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def catbook_home():
    cats = get_all_cats()
    return render_template("home.html", cats=cats)
@app.route('/cats/<int:id>' , methods=['GET', 'POST'])
def catbook_profile(id):
	if request.method == 'GET':
		cat=get_cat_id(id)
		return render_template("cat.html", n=cat)
	else:
		add_vote(id)
		cats = get_all_cats()
		return render_template("home.html", cats=cats)
	

@app.route('/add', methods=['GET', 'POST'])
def catbook_add():
	if request.method == 'GET':
		return render_template("add.html")
	else:
		name=request.form['name']
		create_cat(name)
		cats = get_all_cats()
		return render_template("home.html", cats=cats)

if __name__ == '__main__':
   app.run(debug = True)
