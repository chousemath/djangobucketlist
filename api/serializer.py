from rest_framework import serializers
from .models import Bucketlist

"""
Serializers can be thought sort of as Django forms, they represent your data
over the wire
"""
class BucketlistSerializer(serializers.ModelSerializer):
    """maps model instance into json"""
    class Meta:
        """maps serializer's fields with model's fields"""
        # tell serializer what model we are trying to serialize
        model = Bucketlist
        # tell serializer what data we are trying to represent
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')
