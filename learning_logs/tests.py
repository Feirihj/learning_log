from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Entry, Topic


class LearningLogTests(TestCase):
    def setUp(self):
        self.alice = User.objects.create_user("alice", password="pass12345")
        self.bob = User.objects.create_user("bob", password="pass12345")
        self.topic = Topic.objects.create(text="Python", owner=self.alice)
        self.entry = Entry.objects.create(topic=self.topic, text="Первая запись")

    def test_topics_requires_login(self):
        response = self.client.get(reverse("learning_logs:topics"))
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse("accounts:login"), response.url)

    def test_owner_sees_topic(self):
        self.client.login(username="alice", password="pass12345")
        response = self.client.get(reverse("learning_logs:topic", args=[self.topic.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Первая запись")

    def test_other_user_gets_404(self):
        self.client.login(username="bob", password="pass12345")
        response = self.client.get(reverse("learning_logs:topic", args=[self.topic.id]))
        self.assertEqual(response.status_code, 404)

    def test_new_topic_sets_owner(self):
        self.client.login(username="bob", password="pass12345")
        self.client.post(reverse("learning_logs:new_topic"), {"text": "Django"})
        self.assertTrue(Topic.objects.filter(text="Django", owner=self.bob).exists())

    def test_edit_entry(self):
        self.client.login(username="alice", password="pass12345")
        self.client.post(
            reverse("learning_logs:edit_entry", args=[self.entry.id]),
            {"text": "Обновлено"},
        )
        self.entry.refresh_from_db()
        self.assertEqual(self.entry.text, "Обновлено")
