from flask import Blueprint, request, render_template
from models.Task import Task


task_blueprint = Blueprint("task_controller", __name__)


tasks = [
    Task(1, "Shopping"),
    Task(2, "Study for the test"),
    Task(3, "Clean the house"),
]  # Exercise 4.2


@task_blueprint.route("/", methods=["GET", "POST"])  # Exercise 4.7
def tasks_view():
    if request.method == "POST":  # Exercise 4.9
        title = request.form["title"]
        new_task = Task(len(tasks) + 1, title)
        tasks.append(new_task)

    return render_template("tasks.html", tasks=tasks)


@task_blueprint.route("/complete/<int:task_id>")  # Exercise 4.10
def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True

    return render_template("tasks.html", tasks=tasks)
