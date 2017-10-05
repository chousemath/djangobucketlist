from rest_framework import generics
from .serializer import BucketlistSerializer
from .models import Bucketlist

# Create your views here.
# ListCreateAPIView is generic view which provides GET (list all) / POST method
# handlers
class CreateView(generics.ListCreateAPIView):
    """defines create behavior of rest api"""
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """save post data when creating new bucketlist"""
        serializer.save()
