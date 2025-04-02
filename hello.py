from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

#def index():
    #return "<h1>Hello World</h1>"

def index():
    favorite_cars = ["G-wagon", "Toyota", "Mercendes", "BWM", "Jeep", 100]
    first_name = "Hillary"
    stuff = 'This is a <strong> bold move to make </strong>'
    return render_template("index.html", first_name=first_name, stuff=stuff,
    favorite_cars=favorite_cars)

@app.route("/user/<name>")

def user(name):
    return render_template("user.html", username=name)

#creating custom error page.abs
#invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# internal server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500