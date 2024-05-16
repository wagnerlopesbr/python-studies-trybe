from flask import Flask, render_template, request, redirect
#  render_template: to render a template from the templates folder
#  request: to access the request data
#  redirect: to redirect to another route


app = Flask(__name__)


students_list = [
    {"name": "John Doe", "enrollment": "1234"},
    {"name": "Jane Doe", "enrollment": "91011"},
    {"name": "John Smith", "enrollment": "121314"},
    {"name": "Jane Smith", "enrollment": "151617"}
]


""" I'm using only GET and POST methods
    because I'm using a form in the HTML file
    and I'm not using AJAX
    and HTML forms only support GET and POST methods. """

#  Exercise 1.01
@app.route("/")
@app.route("/students")
def show_students():
    return render_template("students_1.html", students=students_list)


#  Exercise 1.02
@app.route("/create", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        name = request.form["name"]
        enrollment = request.form["enrollment"]
        new_student = {"name": name, "enrollment": enrollment}
        students_list.append(new_student)
        return redirect("/")
    else:
        return render_template("create_student_1.html")


def index_validation(index):
    if index < 0 or index >= len(students_list):
        return redirect("/")


#  Exercise 1.03
@app.route("/update/<int:index>", methods=["GET", "POST"])
def update_student(index):
    index_validation(index)
    student = students_list[index]
    if request.method == "POST":
        name = request.form["name"]
        enrollment = request.form["enrollment"]
        students_list[index] = {"name": name, "enrollment": enrollment}
        return redirect("/")
    else:
        return render_template(
            "update_student_1.html",
            student=student,
            index=index
        )


#  Exercise 1.04
@app.route("/delete/<int:index>", methods=["GET", "POST"])
def delete_student(index):
    index_validation(index)
    if request.method == "POST":
        students_list.pop(index)
        return redirect("/")
    else:
        student = students_list[index]
        return render_template("delete_student_1.html", student=student, index=index)


if __name__ == "__main__":
    app.run(debug=True, port=8080)
