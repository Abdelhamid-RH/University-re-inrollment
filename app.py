from flask import Flask, render_template, request
import csv


app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods = ["POST"])
def result():
    updated = False
    already_inrolled = False

    stdlist = []

    with open("students.csv", "r") as f:
        reader = csv.DictReader(f)
        header = reader.fieldnames
        for row in reader:
            if row["first_name"] == request.form.get("first_name") and row["last_name"] == request.form.get("last_name") and row["id"] == request.form.get("id") and row["status"] == "25/26":
                updated = True
                row["status"] = "26/27"
                stdlist.append(row)
            elif row["first_name"] == request.form.get("first_name") and row["last_name"] == request.form.get("last_name") and row["id"] == request.form.get("id") and row["status"] == "26/27":
                already_inrolled = True
                stdlist.append(row)
            else:
                stdlist.append(row)

    full_name = request.form.get("first_name") + " " + request.form.get("last_name")

    if updated == True:
        with open("students.csv", "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames = header)
            writer.writeheader()
            writer.writerows(stdlist)
        return render_template("success.html", name = full_name, email = request.form.get("email"))
    elif already_inrolled == True:
        return render_template("already.html", name = full_name)
    else:
        return render_template("failure.html")

        
