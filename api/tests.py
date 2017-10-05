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
    """test suite for api views, sort of like controller tests in Rails"""
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

    def test_api_can_get_a_bucketlist(self):
        """test api has bucketlist get capabilities"""
        # I think what is happening is that
        # get the first bucketlist in the database
        bucketlist = Bucketlist.objects.get()
        # http://www.django-rest-framework.org/api-guide/testing/#apiclient
        response = self.client.get(
            # 'reverse' should represent the 'view' name (name in urls.py)
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Asserts that a Response instance produced the given status_code and
        # that -->text<-- appears in the content of the response, in this case
        # 'bucketlist' is the text
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """test that api has bucketlist update capabilities"""
        # get first bucketlist in database
        bucketlist = Bucketlist.objects.get()
        bucketlist_changed = {'name': 'changedname'}
        response = self.client.put(
            reverse('details', kwargs={'pk': bucketlist.id}),
            bucketlist_changed,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        bucketlist = Bucketlist.objects.get()
        self.assertEqual(bucketlist.name, 'changedname')

    def test_api_can_delete_bucketlist(self):
        """test that api has bucketlist delete capabilities"""
        bucketlist_count_before = Bucketlist.objects.count()
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            # If your request used the follow argument, the expected_url and
            # target_status_code will be the url and status code for the final
            # point of the redirect chain
            follow=True
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Bucketlist.objects.count(), bucketlist_count_before - 1)

