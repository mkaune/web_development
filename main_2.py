from flask import Flask, render_template

from other.control3 import second

app=Flask(__name__)
app.register_blueprint(second, url_prefix="/private") #con /admin pasamos a blueprint.py ahi otros templates, etc.

@app.route("/home") #/home 
@app.route("/") #/ dan acceso a test1 


def test():
    return "<h1>Main2<h2>"
    
if __name__== "__main__":
   
    app.run()
    