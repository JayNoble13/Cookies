from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_app.models.cookie import Cookie

@app.route('/')
def home():
    return redirect('/dashboard')

@app.route('/add')
def add():
    return render_template ("new.html")


@app.route("/create", methods=['POST'])
def create():
    if not Cookie.validate_cookie(request.form):
        return redirect('/add')
    data={
        "cookietype": request.form["cookietype"],
        "buyer": request.form["buyer"],
        "numb_box": request.form["numb_box"],
    }
    Cookie.create(data)
    return redirect("/dashboard")

@app.route('/dashboard')
def index():
    cookie=Cookie.get_all()
    return render_template("dashboard.html", cookies=cookie)

@app.route("/edit/<int:id>")
def edit(id):
    data= {
        "id":id
    }
    return render_template("edit.html", cookie=Cookie.get_one(data))

@app.route("/update/cookie", methods=['POST'])
def update():
        if not Cookie.validate_cookie(request.form):
            return redirect('/add')
        data={
            "cookietype": request.form["cookietype"],
            "buyer": request.form["buyer"],
            "numb_box": request.form["numb_box"],
            "id": request.form["id"],
        }
        Cookie.update(data)
        return redirect('/dashboard')