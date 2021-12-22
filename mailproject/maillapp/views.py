from django.shortcuts import render
from django.views.generic.list import ListView  # basic listviews of objects
from django.views.generic.detail import DetailView #detail view used to show details for single single objetcs
#create views creates item in database and update views updates it
from django.views.generic.edit import CreateView ,UpdateView, DeleteView
from django.urls import reverse_lazy #to redirect the user over a page 
#lgin and logout
# #database
from .models import Task 
# model = task // task is a class in model.py // database so that it could acces the values

class HomePageView(ListView):
    model = Task
    context_object_name = 'task'
    template_name = 'maillapp/tasklist.html'
    def get_context_data(self, **kwargs):
        count = 0
        context = super().get_context_data(**kwargs)
        for item in Task.objects.all():
            if item.complete == False:
                count += 1  
        context['count'] = count
        return context

class TaskDetail( DetailView):
    model = Task
    template_name = 'maillapp/taskdetail.html' 
    
class TaskCreate( CreateView): #fo inserting objects in database
    model = Task
    template_name = 'maillapp/taskform.html' 
    fields = {'desc', 'title' } 
    success_url = reverse_lazy('app_pge')  #name of urls in ('')
    
class TaskUpdate(UpdateView): #to update already existed objects in TaskCreate
    model = Task
    fields = {'title', 'desc', 'complete'} 
    template_name = 'maillapp/taskform.html' #it searches for file which is seracged by TaskCreate
    success_url = reverse_lazy('app_pge')

class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task' 
    success_url = reverse_lazy('app_pge')
    template_name = 'maillapp/taskdelete.html' 
