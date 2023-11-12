from flask_app import app
from flask import render_template, request, redirect
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", dojos = dojos)

@app.route('/create_dojo', methods=["POST"])
def create_dojo():
    data = {
        "name" : request.form["name"]
    }
    Dojo.save(data)
    print("Dojo Created!")
    return redirect("/")

@app.route('/dojos/<int:dojo_id>')
def show_dojo(dojo_id):
    dojo = Dojo.get_dojo_with_ninjas(dojo_id)
    print("dojo")
    return render_template("city_ninjas.html", dojo = dojo)

@app.route('/delete/<int:id>')
def delete(id):
    Dojo.delete(id)
    return redirect('/')