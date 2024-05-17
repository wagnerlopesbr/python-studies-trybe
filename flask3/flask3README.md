# Flask Exercises

## Exercise 1

Create a Flask application that renders a template called index.html. The template should display a welcome message on the page. The welcome message should be passed as an argument to the render_template function. Additionally, ensure that the template is properly configured with the basic HTML structure.

---

## Exercise 2

Create a Flask application that renders a template called book.html. The template should receive information about a book, such as title, author, and publication year, and display them on the page.

#### Model:

1. Create a class called Book that represents a book, with the attributes title, author, and year.
2. Create a book object with information about a book of your choice.

#### View:

3. Create a template called book.html that displays the book's information.
4. Use Jinja2 syntax to display the book's title, author, and publication year.

#### Controller:

5. Create a route / that renders the book.html template.
6. Pass the book object as an argument to the render_template function.

---

## Exercise 3

Create a web application using Flask and Jinja2 that displays a list of movies. Follow the step-by-step guide:

1. Create a route / that renders a template called index.html.
2. The index.html template should display the title "Movie List" at the top of the page.
3. Define a list of movies in the application file and pass this list to the template.
4. In the template, use a Jinja2 loop structure to display each movie from the list in an HTML list.
5. Each movie should be displayed as a list item, containing the movie title and release year.
6. Style the movie list using CSS to make it visually appealing.

#### Tips:

- Use Flask's render_template function to render the index.html template.
- Pass the list of movies to the template as an argument in the render_template function.
- In the template, use Jinja2 syntax to iterate over the list of movies and display them.
- Use separate CSS files to style the movie list, if desired.

---

## Exercise 4

You have been hired to develop a task management web application using Flask and Jinja2 templates. The application should allow users to add, view, and mark tasks as completed.

## Model:

1. Create a class named Task representing a task, with the attributes id, title, and completed.
2. Create a list of tasks in the application file and initialize it with some example tasks.

## View:

3. Create a template named tasks.html that displays the list of tasks and provides a form for adding new tasks.
4. Use a Jinja2 loop structure to iterate over the list of tasks and display them on the page.
5. Add a completion marking button for each displayed task, allowing users to mark a task as completed.
6. Style the page using CSS to make it visually appealing.

## Controller:

7. Create a route '/' that renders the tasks.html template.
8. In the template, add a form for adding new tasks.
9. When the user submits a new task, the route should add the task to the list of tasks.
10. Add an additional route '/complete/int:task_id' that is triggered when a user marks a task as completed. This route should update the state of the corresponding task in the list of tasks.

## Tips:

- Create a separate file for the Task class and import it into the Flask application file.
- Use Flask's render_template function to render the tasks.html template.
- Pass the list of tasks to the template as an argument in the render_template function.
- In the template, use Jinja2 syntax to iterate over the list of tasks and display them.
- Use separate CSS files to style the page if desired.
- Use the POST method to submit the task addition form, and use the GET method to mark tasks as completed in the '/complete/int:task_id' route.
- In the '/complete/int:task_id' route, update the state of the corresponding task in the list of tasks based on the received task_id parameter.
