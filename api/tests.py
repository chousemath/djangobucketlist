from django.test import TestCase
from .models import Bucketlist

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
