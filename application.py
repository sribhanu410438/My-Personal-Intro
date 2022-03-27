from flask import Flask, request, render_template
application = Flask(__name__)

application.route("/")
def hello():
    return render_template ("index.html")

application.route("/newproject")
def newproject():
    return render_template ("newproject.html")

application.route("/projects")
def projects():
    return render_template ("projects.html")

application.route("/education")
def education():
    return render_template ("education.html")

application.route("/skillset")
def skillset():
    return render_template ("skillset.html")

# application.route('/newprojects', methods=['POST'])
# def saveproject():
#     input_nopol = request.form['text_box']
#     if request.method == 'POST':
#        with open('nopol.txt', 'w') as f:
#             f.write(str(input_nopol))
#     return render_template('index.html', nopol=input_nopol)
