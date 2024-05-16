from flask import Flask, render_template, request, redirect
#  render_template: to render a template from the templates folder
#  request: to access the request data
#  redirect: to redirect to another route
from models.student_model import StudentModel


app = Flask(__name__)


""" I'm using only GET and POST methods
    because I'm using a form in the HTML file
    and I'm not using AJAX
    and HTML forms only support GET and POST methods. """

#  Exercise 2.03
@app.route("/")
@app.route("/students")
def show_students():
    students = StudentModel.find()
    dict_students = [student.to_dict() for student in students]
    return render_template("students_2.html", students=dict_students)


#  Exercise 2.03
@app.route("/create", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        name = request.form["name"]
        enrollment = request.form["enrollment"]
        new_student = {"name": name, "enrollment": enrollment}
        StudentModel(new_student).create()
        return redirect("/")
    else:
        return render_template("create_student_2.html")


#  Exercise 2.03
@app.route("/update/<int:index>", methods=["GET", "POST"])
def update_student(index):
    print(index)
    student = StudentModel.find_one({"enrollment": str(index)})
    if not student:
        return redirect("/")
    if request.method == "POST":
        name = request.form["name"]
        enrollment = request.form["enrollment"]
        updated_student = {"name": name, "enrollment": enrollment}
        student.update(updated_student)
        return redirect("/")
    else:
        return render_template(
            "update_student_2.html",
            student=student.to_dict(),
            index=index
        )


#  Exercise 2.03
@app.route("/delete/<int:index>", methods=["GET", "POST"])
def delete_student(index):
    student = StudentModel.find_one({"enrollment": str(index)})
    if request.method == "GET":
        return render_template("delete_student_2.html", student=student.to_dict(), index=index)
    if not student:
        return redirect("/")
    student.delete()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
