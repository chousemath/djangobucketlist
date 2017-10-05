from rest_framework import generics
from .serializer import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
# ListCreateAPIView is generic view which provides GET (list all) / POST method
# handlers
class CreateView(generics.ListCreateAPIView):
    """defines create behavior of rest api"""
    # query set is the collection of items we are trying to view
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
