from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task


class TaskManagerAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Get JWT token
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpass123"}
        )
        self.token = response.data["access"]

        self.auth_header = {
            "HTTP_AUTHORIZATION": f"Bearer {self.token}"
        }

    
    # User Authentication test case 

    def test_user_registration(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "newuser",
                "email": "new@test.com",
                "password": "strongpass123"
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_login(self):
        response = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "testuser", "password": "testpass123"}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)


    # Authorization Test Case
    def test_unauthenticated_user_cannot_create_task(self):
        response = self.client.post(
            reverse("task-list"),
            {"title": "Task 1", "description": "Test"}
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Test Cases for CRUD Operations

    # 1) Test Case - Create
    def test_create_task(self):
        response = self.client.post(
            reverse("task-list"),
            {"title": "Task 1", "description": "Test"},
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # View list of task - READ
    def test_get_all_tasks(self):
        Task.objects.create(user=self.user, title="Task A")

        response = self.client.get(
            reverse("task-list"),
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #View Single Task - READ
    def test_get_single_task(self):
        task = Task.objects.create(user=self.user, title="Task A")

        response = self.client.get(
            reverse("task-detail", args=[task.id]),
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 3) Test Case -  Update
    def test_update_task(self):
        task = Task.objects.create(user=self.user, title="Old Title")

        response = self.client.put(
            reverse("task-detail", args=[task.id]),
            {
                "title": "Updated Title",
                "description": "",
                "completed": True
            },
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # 4)- Test Case - Delete
    def test_delete_task(self):
        task = Task.objects.create(user=self.user, title="To Delete")

        response = self.client.delete(
            reverse("task-detail", args=[task.id]),
            **self.auth_header
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)