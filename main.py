from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template ("index.html")

@app.route("/newproject")
def newproject():
    return render_template ("newproject.html")

@app.route("/projects")
def projects():
    return render_template ("projects.html")

@app.route("/education")
def education():
    return render_template ("education.html")

@app.route("/skillset")
def skillset():
    return render_template ("skillset.html")

if __name__ == "__main__":
    app.run()