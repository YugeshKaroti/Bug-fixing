# Step -1 : Importing the Flask Library

from flask import Flask, render_template, request

# Step-2 : Creating an flask objeect with __name__ parameter

app = Flask(__name__)

# Step-3 : Creating an endpoint/route and bind each route with some functionality

notes = []
@app.route('/', methods=["GET","POST"])
def index():
    if request.method=="POST":
        note = request.form.get("note","")
        notes.append(note)
    return render_template("home.html", notes=notes)

# Step-4 : Run the application

if __name__ == '__main__':
    app.run(debug=True)