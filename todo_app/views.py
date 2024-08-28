from django.shortcuts import render
from todo_app.models import Todo
from django.http import HttpResponseRedirect

# View to display the list of all Todo items
def todo_list(request):
    # Retrieve all Todo objects from the database
    todos = Todo.objects.all()
    # Render the 'todo_list.html' template with the list of todos
    return render(
        request,
        "bootstrap/todo_list.html",
        {"todos": todos},  # Pass the todos as context to the template
    )

# View to delete a specific Todo item
def todo_delete(request, pk):
    # Get the specific Todo object by primary key (id)
    todo = Todo.objects.get(id=pk)
    # Delete the retrieved Todo object from the database
    todo.delete()
    # Redirect to the home page (or the list view) after deletion
    return HttpResponseRedirect("/")

# View to create a new Todo item
def todo_create(request):
    # Print the HTTP method used (for debugging purposes)
    print(request.method)
    
    # If the request method is GET, render the creation form
    if request.method == "GET":
        return render(request, "bootstrap/todo_create.html")
    else:
        # If the request method is POST, create a new Todo object with the data from the form
        Todo.objects.create(
            title=request.POST["title"],  # Get the title from the form data
            description=request.POST["description"],  # Get the description from the form data
        )
        # Redirect to the home page after creating the new Todo
        return HttpResponseRedirect("/")

# View to update an existing Todo item
def todo_update(request, pk):
    # If the request method is GET, retrieve the specific Todo object and render the update form
    if request.method == "GET":
        todo = Todo.objects.get(id=pk)
        return render(request, "bootstrap/todo_update.html", {"todo": todo})
    else:
        # If the request method is POST, update the existing Todo object with the new data
        todo = Todo.objects.get(id=pk)
        todo.title = request.POST["title"]  # Update the title
        todo.description = request.POST["description"]  # Update the description
        todo.save()  # Save the changes to the database
        # Redirect to the home page after updating the Todo
        return HttpResponseRedirect("/")
