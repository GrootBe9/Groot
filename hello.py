from flask import Flask, render_template, flash, request, url_for, redirect, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm
import mainCode, model 
app = Flask(__name__)
# app.secret_key = "super secret key"
app.config["SECRET_KEY"] = "484064281fc536fe3e27134787b8e13b"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
pointer=-1
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60),  nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"

@app.route("/")
def homepage():
    return render_template("myindex.html")


@app.route("/signup/", methods=["GET", "POST"])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.name.data}!", "success")
        return redirect(url_for("chat"))
    return render_template("signup.html", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "lol@lol.in" and form.password.data == "password":
            flash(f"You have been logged in!", "success")
            return redirect(url_for("chat"))
        else:
            flash(f"Login Unsucessful. Please check email and password.", "danger")
    return render_template("login.html", form=form)


@app.route("/chat/",methods=['GET','POST'])
def chat():
    global pointer
    if request.method=='POST':
        pointer=pointer+1
        req_data=request.form['message']
        print(req_data)
        print("pointer= ", pointer)
        #message=req_data['message']
        return jsonify({'message' : mainCode.myfunc(req_data,pointer)})
        #return jsonify({'message' : next(model.myfunc(req_data,pointer)) })
        #return mainCode.myfunc(req_data)
    try:
        return render_template("chat.html")
    except Exception as e:
        return render_template("500.html", error=e)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


if __name__ == "__main__":
    app.run(debug=True)

