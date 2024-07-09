from django.views.generic.list import ListView
from .models import Task
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

# ここで、list_todo関数を定義して、task.htmlを返す
class list_todo(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task.html'

class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    template_name = 'task_form.html'
    success_url = reverse_lazy('todolist:tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name = 'task_Update.html'
    success_url = reverse_lazy('todolist:tasks')

class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    template_name = 'task_delete.html'
    success_url = reverse_lazy('todolist:tasks')
