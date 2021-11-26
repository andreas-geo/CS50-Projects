import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

app = Flask(__name__)



app.config["TEMPLATES_AUTO_RELOAD"] = True






app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///VehicleInsider.db")




@app.route("/")
def index():
   return render_template("index.html")



@app.route("/Polo")
def Polo():
    return render_template("Polo.html")

@app.route("/Mii")
def Mii():
    return render_template("Mii.html")

@app.route("/Vito")
def Vito():
    return render_template("Vito.html")

@app.route("/Eclass")
def Eclass():
    return render_template("Eclass.html")

@app.route("/Wrangler")
def Wrangler():
    return render_template("Wrangler.html")

@app.route("/Karpathos")
def Karpathos():
    return render_template("Karpathos.html")

@app.route("/Heraklion")
def Heraklion():
    return render_template("Heraklion.html")

@app.route("/Rhodes")
def Rhodes():
    return render_template("Rhodes.html")

@app.route("/Santorini")
def Santorini():
    return render_template("Santorini.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        result_checks = is_provided("FirstName") or is_provided("LastName") or is_provided("BirthDay") or is_provided("BirthMonth") or is_provided("BirthYear") or is_provided("EmailAddress") or is_provided("PhoneNumber")  or is_provided("Username")  or is_provided("Password")  or is_provided("Confirmation")
        if result_checks != None:
            return result_checks
        if request.form.get("Password") != request.form.get("Confirmation"):
            return apology("Passwords do not match")
        k = db.execute("INSERT INTO USERS (FirstName,LastName,BirthDay,BirthMonth,BirthYear,EmailAddress,PhoneNumber,Username, Hash) VALUES (:FirstName,:LastName,:BirthDay,:BirthMonth,:BirthYear,:EmailAddress,:PhoneNumber,:Username, :Hash)",
        FirstName=request.form.get("FirstName"),
        LastName=request.form.get("LastName"),
        BirthDay=request.form.get("BirthDay"),
        BirthMonth=request.form.get("BirthMonth"),
        BirthYear=request.form.get("BirthYear"),
        EmailAddress=request.form.get("EmailAddress"),
        PhoneNumber=request.form.get("PhoneNumber"),
        Username=request.form.get("Username"),
        Hash=generate_password_hash(request.form.get("Password")))

        #except:
            #return apology("username already exists", 403)
        if k is None:
            return apology("registration error", 403)
        session["user_id"] = k
        return redirect("/")
    else:
        return render_template("register.html")

def is_provided(domain):
    if not request.form.get(domain):
        return apology(f"must provide {domain}", 403)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""


    session.clear()

    if request.method == "POST":

        result_checks = is_provided("Username") or is_provided("Password")
        if result_checks is not None:
            return result_checks

        rows = db.execute("SELECT * FROM USERS WHERE Username = :Username",
                         Username=request.form.get("Username"))

        if len(rows) != 1 or not check_password_hash(rows[0]["Hash"], request.form.get("Password")):
            return apology("invalid Username and/or password", 403)

        session["user_id"] = rows[0]["Username"]

        return redirect("/")

    else:
        return render_template("login.html")

@app.route("/rent", methods=["GET", "POST"])
@login_required
def rent():
    """Rent A motor vehicle"""

    if request.method == "POST":
        result_checks = is_provided("Vehicle") or is_provided("Location") or is_provided("DateOfDelivery") or is_provided("TimeOfDelivery") or is_provided("DateOfReturn") or is_provided("TimeOfReturn")
        if result_checks != None:
            return result_checks
        r = db.execute("INSERT INTO RENTALS (Vehicle,Location,DateOfDelivery,TimeOfDelivery,DateOfReturn,TimeOfReturn,Username1) VALUES (:Vehicle,:Location,:DateOfDelivery,:TimeOfDelivery,:DateOfReturn,:TimeOfReturn,:Username1)",

        Vehicle=request.form.get("Vehicle"),
        Location=request.form.get("Location"),
        DateOfDelivery=request.form.get("DateOfDelivery"),
        TimeOfDelivery=request.form.get("TimeOfDelivery"),
        DateOfReturn=request.form.get("DateOfReturn"),
        TimeOfReturn=request.form.get("TimeOfReturn"),
        Username1 = session["user_id"])

        if r is None:
            return apology("Error with Rental", 403)
        session["Username1"] = r

        flash("Rental Successful")
        return redirect("/")

    else:
        return render_template("rent.html")




@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


for code in default_exceptions:
    app.errorhandler(code)(errorhandler)





