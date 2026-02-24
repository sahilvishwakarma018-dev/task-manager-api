from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from .permissions import IsOwnerOrAdmin
from rest_framework.pagination import PageNumberPagination
from .serializers import TaskSerializer, UserRegisterSerializer
from .models import Task

#API to Register User
class RegisterAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#API to Create New Task & view task in list format
class TaskListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        
        if request.user.is_staff:
            tasks = Task.objects.all()
        else:
            tasks = Task.objects.filter(user=request.user)

        tasks = self.filter_tasks(request, tasks)

        # Pagination
        paginator = PageNumberPagination()
        paginator.page_size = 5
        result_page = paginator.paginate_queryset(tasks, request)
        serializer = TaskSerializer(result_page, many=True)

        return paginator.get_paginated_response(serializer.data)

    def filter_tasks(self, request, queryset):
        completed = request.query_params.get("completed")
        if completed is not None:
            return queryset.filter(completed=completed.lower() == "true")
        return queryset

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

#API to Update, Delete and Read Single record 
class TaskDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrAdmin]

    def get_object(self, pk):
        task = get_object_or_404(Task, pk=pk)
        self.check_object_permissions(self.request, task)
        return task

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({"message": "Task deleted successfully"},status=status.HTTP_204_NO_CONTENT)
