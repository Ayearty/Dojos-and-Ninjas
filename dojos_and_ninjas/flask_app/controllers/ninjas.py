from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route("/ninjas")
def new_ninja_form():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojos)
#Were not displaying any data so we dont need a get_all method.

@app.route("/create_ninja", methods=["POST"])
def create_ninja():
    data = {
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "age":request.form["age"],
        "dojo_id":request.form["dojo_id"]
    }
    Ninja.save(data)
    return redirect('/')

@app.route('/delete_ninja/<int:id>')
def delete_ninja(id):
    Ninja.delete(id)
    return redirect('/')
