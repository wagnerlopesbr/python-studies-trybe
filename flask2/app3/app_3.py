from flask import Flask, render_template, request
from controllers.film_controller import FilmController


app = Flask(__name__)
film_controller = FilmController()


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title")
        movies = film_controller.search_movies_by_title(title)
    else:
        movies = film_controller.search_movies_by_title()
    return render_template("index.html", movies=movies)


@app.route("/movies/<_id>")
def movie(_id):
    print(_id)
    movie = film_controller.search_movie_by_id(_id)
    return render_template("movie.html", movie=movie)


if __name__ == "__main__":
    app.run(debug=True)