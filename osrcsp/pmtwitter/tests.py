
from django.apps import apps
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestAPI(APITestCase):

  fixtures = ["data.json"]

  @classmethod
  def setUpClass(cls):
    super(TestAPI, cls).setUpClass()
    cls.Tweet = apps.get_model("pmtwitter.Tweet")

  def testCreateSuccess(self):
    url = reverse("v1:tweet-list")
    resp = self.client.post(url, {"name": "n" * 20, "message": "m" * 50})
    self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

  def testCreateFail(self):
    url = reverse("v1:tweet-list")
    resp = self.client.post(url, {"name": "n" * 21, "message": "m" * 51})
    self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
    self.assertIn("name", resp.data)
    self.assertIn("message", resp.data)

  def testList(self):
    url = reverse("v1:tweet-list")
    resp = self.client.get(url)
    self.assertEqual(resp.status_code, status.HTTP_200_OK)
    self.assertEqual(len(resp.data), 4)
