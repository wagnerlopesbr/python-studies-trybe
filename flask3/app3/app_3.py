from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    movies = [
        {'title': 'O Poderoso Chefão', 'year': 1972},
        {'title': 'Interestelar', 'year': 2014},
        {'title': 'A Origem', 'year': 2010},
        {'title': 'Clube da Luta', 'year': 1999},
        {'title': 'Pulp Fiction', 'year': 1994}
    ]
    return render_template('index.html', movies=movies)

if __name__ == '__main__':
    app.run()
