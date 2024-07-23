from django import forms
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

# tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    # priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
 
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# Add a new task:
def add(request):

    # Check if method is POST
    if request.method == "POST":
        form = NewTaskForm(request.POST) # request.post is what the user submitted
        # Check if form data is valid (server side)
        if form.is_valid():
            task = form.cleaned_data["task"] # isolate the task from the 'cleaned' version of form data
            # tasks.append(task) # add the new task to our list of tasks
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index")) # redirect user to list of tasks
        else:
            # if form invalid, re-render the page with existing infomation
            return render(request, "task/add.html", {
                "form": form
            })

    # GET the page, not POST/submit
    return render(request, "tasks/add.html", {
        "form": NewTaskForm()
    })


