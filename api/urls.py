from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^bucketlists/$', views.CreateView.as_view(), name='create'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.DetailsView.as_view(), name='details'),
]

# allows us to specify the data format (raw json or even html) when we use the
# URLs. It appends the format to be used to every URL in the pattern
urlpatterns = format_suffix_patterns(urlpatterns)
