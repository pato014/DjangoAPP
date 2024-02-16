from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task
from .forms import TaskForm



class TaskListView(ListView):
    model = Task
    template_name = 'taskmanager/task_list.html'
    context_object_name = 'tasks'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'taskmanager/task_detail.html'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/taks_form.html'
    success_url = reverse_lazy('task_list')

class TaskUpdateView(UpdateView):

    model = Task
    form_class = TaskForm
    template_name = 'taskmanager/taks_form.html'
    success_url = reverse_lazy('task_list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'taskmanager/task_delete_confirm.html'
    success_url = reverse_lazy('task_list')
