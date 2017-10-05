from django.test import TestCase
from .models import Bucketlist
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """defines the test suite for the Bucketlist model"""
    def setUp(self):
        """define test client and other test variables"""
        self.bucketlist_name = 'Write world class code'
        self.bucketlist = Bucketlist(name=self.bucketlist_name)

    def test_model_can_create_a_bucketlist(self):
        """test bucketlist model can create a bucketlist"""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        self.assertNotEqual(Bucketlist.objects.count(), old_count)

class ViewTestCase(TestCase):
    """test suite for api views"""
    def setUp(self):
        """define test client and other test variables"""
        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format='json'
        )

    def test_api_can_create_a_bucketlist(self):
        """test that api has bucketlist creation capabilities"""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
