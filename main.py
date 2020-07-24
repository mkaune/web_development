from flask import Flask, render_template

from admin.blueprint import second

app=Flask(__name__)
app.register_blueprint(second, url_prefix="/private") #con /admin pasamos a blueprint.py ahi otros templates, etc.

@app.route("/home") #/home 
@app.route("/") #/ dan acceso a test1 


def test():
    return "<h1>Main1<h2>"
    
if __name__== "__main__":
    app.run()
    
    
"""
<img src="{{url_for('static',filename='images/ecostaff.png')}}" >

<link rel="stylesheet" type='text/scss' href="{{url_for('static',filename='style.scss')}}" >

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
{% extends "base2.html" %}

<img src="static/images/ecostaff.png" alt="Logo" style="width:500px;height:600px;">

http://exploreflask.com/en/latest/blu...

base2:

<body> 	
<h2>{{Image}}</h2>

You can specify background images<br>
for any visible HTML element.<br>
In this example, the background image<br>
is specified for a div element.<br>
By default, the background-image<br>
will repeat itself in the direction(s)<br>
where it is smaller than the element<br>
where it is specified. (Try resizing the<br>
browser window to see how the<br>
background image behaves.
</div>

</body>

</html>



"""