from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.
class Bucketlist(models.Model):
    """this class represents the Bucketlist model"""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        """return human-friendly identifier for admin backoffice"""
        return self.name

@receiver(pre_save, sender=Bucketlist)
def bucketlist_pre_save(sender, instance, *args, **kwargs):
    if len(instance.name) < 5:
      instance.name += '<-LESS-THAN-5-CHARS-FROM-PRE-SAVE-SIGNAL'
