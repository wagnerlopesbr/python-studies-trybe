from flask import Flask
from controllers import TaskController


app = Flask(__name__)


app.register_blueprint(TaskController.task_blueprint)


if __name__ == "__main__":
    app.run()
