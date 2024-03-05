from django.test import TestCase
from django.urls import reverse
from .models import Idea
from django.contrib.auth.models import User

class IdeaModelTestCase(TestCase):
    def test_idea_creation(self):
        user = User.objects.create(username='testuser')
        idea = Idea.objects.create(title='Test Idea', description='This is a test idea', author=user)
        self.assertEqual(idea.title, 'Test Idea')
        self.assertEqual(idea.description, 'This is a test idea')
        self.assertEqual(idea.author, user)

class ViewsTestCase(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_add_idea_view(self):
        response = self.client.get(reverse('add_idea'))
        self.assertEqual(response.status_code, 302)