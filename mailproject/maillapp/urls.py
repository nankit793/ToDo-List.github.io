from os import name
from django.urls import path
from .views import HomePageView, TaskDetail, TaskCreate, TaskUpdate ,TaskDelete
urlpatterns = [
    path('', HomePageView.as_view(), name='app_pge'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'), 
    path('create/', TaskCreate.as_view(), name='task_create') ,
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task-update')
]
 