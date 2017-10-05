from rest_framework import generics
from .serializer import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
# ListCreateAPIView is generic view which provides GET (list all) / POST method
# handlers
# APIView is the base class, takes care of all the routing for you
class CreateView(generics.ListCreateAPIView):
    """defines create behavior of rest api"""
    # query set is the collection of items we are trying to view
    # ListCreateAPIView takes of GET and POST for you, you use this because
    # this endpoint only supports a list of objects
    # DRF responses are completely unrendered, they return DATA and status_code
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """save post data when creating new bucketlist"""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """
    RetrieveUpdateDestroyAPIView is a generic view that provides GET(one),
    PUT, PATCH and DELETE method handlers
    """
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
