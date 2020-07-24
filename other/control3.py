from flask import Flask, redirect, url_for, render_template, request, session, flash, Blueprint
#session temporary, store on the serve, pass around the server
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

#second=Blueprint("second",__name__, static_folder="static", template_folder="templates")

app = Flask(__name__)
app.secret_key="papo"
app.config['SQLALCHEMY_DATABSE_URI'] = 'sqlite:///users.sqlite3' #users name of the table
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#add extra for no warnings
app.permanent_session_lifetime=timedelta(minutes =5)#store permanent session data for 5 min


db=SQLAlchemy(app)
#easy to store data with python
#objects store in rows and columns, (ind. items pieces of info)
#we want objects with name and email
class users(db.Model):
    _id=db.Column("Id", db.Integer, primary_key=True ) #each object has an unique id and 
    #can be int. string. it needds to be unique. pk=True way me reference our objects.
    #when we search for object no errors thanks to uniquees
    name=db.Column(db.String(100))
    email=db.Column(db.String(100))

    def __init__(self, name, email):
        self.name=name
        self.email=email
        #users object has atributes name,email as columns of data
        
#second=Blueprint("second",__name__, static_folder="static", template_folder="templates")  
@app.route("/")
def home():
    return render_template("template.html")

@app.route("/view") #<usr> input parameter

def view():
    return render_template("view.html" ,values=users.query.all())

@app.route("/<name>")
def general(name):
    return render_template("base2.html", Image=name)   
    

@app.route("/login", methods=["POST", "GET"])
def login():
    #form action=# , method=post! input type: text/submit
    #print("here we are")
    if request.method == "POST":
        #print("here we are")
        session.permanent=True
        #last 5min if we close browser
        #with false is going to last as long your in your browser
        user = request.form["nm"]
        #input in text form : name="nm"
        session["user"] = user 
        #save data in session
        """flash("Login succesful")
        return redirect(url_for("user"))"""

        found_user=users.query.filter_by(name=user).first() #users data base object
        """filter_by  looks for certain properties
        first we finde we return; if change first with all we get all objects with name=user
        if change first with delete we delete this object: commit to secure. 
        
        """
        if found_user:# si ya hay un nombre asi guardado 
            
            session["email"]=found_user.email #en la data base este nombre ya ttiene email
        else:
            usr=users(user,"")
            db.session.add(usr)
            db.session.commit()
        flash("Login succesful")
        return redirect(url_for("user"))
        
    else:
        #si ya hice login una vez, y luego decido volver a /login toncs:
        if "user" in session:
            #me mantengo en /user porque no hace falta volver a logearse
            flash("Already logged in")
            return redirect(url_for("user"))

        return render_template("login.html") #si no hay info de session
        #o sino he hecho submit: render con form 

  
@app.route("/user", methods=["POST", "GET"]) #<usr> input parameter

def user():
    email=None
    #si ya hice login entonces user en session!
    #print("here we are")
    if "user" in session:
        user=session["user"] #esto es el input en login( osea nombre)
        #return f"<h1>{user}</h1>" #antes return simple input (nombre)

        if request.method== "POST":
            #session.permanent=True
            email=request.form["email"]
            #input in "enter email"
            session["email"]= email #save "email" in session dict()
            flash("Email was saved!")

            #ya hubo input de email ahora lo podemos guardar en la db junto al nombre (user)
            found_user=users.query.filter_by(name=user).first() #users data base object
            found_user.email=email #input email
            db.session.commit()
            
            flash("Email was saved!")
        else:
            if email in session:
                email=session["email"]
            
        return render_template("user.html", email=email)
    
    #si escribi user pero no he hecho login entonces redirect
    else:
        flash("you are not logged in")
        return redirect(url_for("login")) #

    
@app.route("/logout")

def logout():
    
    #esto es el input en login( osea nombre)
    flash("You have been logged out", "info")
    session.pop("user",None) #remove user data from session.(remove key)
    session.pop("email",None) #remove email from session when logout
    #vuelta login para volver a logear.
    #tambien se borra si cierro browser
    return redirect(url_for("login"))

if __name__ == "__main__":
    db.create_all()
    app.run()

#when close browsr session data is deleted
