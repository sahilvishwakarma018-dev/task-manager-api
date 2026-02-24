from django.urls import path
from .views import (
    RegisterAPIView,
    TaskListCreateAPIView,
    TaskDetailAPIView,
)

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("tasks/", TaskListCreateAPIView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetailAPIView.as_view(), name="task-detail")
]