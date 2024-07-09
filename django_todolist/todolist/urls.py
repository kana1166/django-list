from django.urls import path
from . import views
from .views import list_todo
from .views import TaskCreate
from .views import TaskUpdate
from .views import TaskDelete


app_name = 'todolist'
urlpatterns = [
    path('',list_todo.as_view(), name='tasks'),
    path('create-task/', TaskCreate.as_view(), name='create-task'),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name='update-task'),
     path('delete-task/<int:pk>/', TaskDelete.as_view(), name='delete-task'),
]


# IndexViewに処理を移す