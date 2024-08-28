from django.urls import path
from todo_app import views

urlpatterns = [
    path("", views.todo_list, name="list"),
    path("delete/<int:pk>/", views.todo_delete, name="delete"),
    path("create/", views.todo_create, name="create"),
    path("update/<int:pk>/", views.todo_update, name="update"),
]
