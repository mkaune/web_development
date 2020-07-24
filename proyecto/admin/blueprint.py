
from flask import Blueprint, render_template

second=Blueprint("second",__name__, static_folder="static", template_folder="templates")

#de main: app.register_blueprint(second, url_prefix="/admin") 


@second.route("/") #/admin/home
@second.route("/name") #/admin/ me da acceso a home

def home():
    #return render_template("home.html")                     
    return render_template("home.html", Image="Ecostaff")                      

@second.route("/private") #admin/private me da acceso a test
def test():
    return "<h1>THIS IS PRIVATE<h1>"

"""
app=Flask(__name__)
@app.route("/home")
@app.route("/")


def test():
    "<h1>Test<h2>"
    
if __name__== "__main__":
    app.run(debug=True)
    """
"""
@app.route("/<name>")
def user(name):
	return f"Hello {name}!"
"""