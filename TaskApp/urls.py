# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import TaskApiView

# router = DefaultRouter()
# router.register(r'tasks', TaskApiView, basename='task')

# urlpatterns = [
#     path('', include(router.urls)),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet
from .views import *

router = DefaultRouter()

router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('tasks/<int:task_id>/edit/', edit_task_form, name='edit_task_form'),
    path('createtask/', CreateTask, name='create-task'),
    path('addtask/', createView, name='createview'),

]


