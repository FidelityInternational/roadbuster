from django.conf.urls import url

from .views import detail_view


urlpatterns = [
    url(r'^detail/([0-9]+)/$', detail_view, name='detail_view'),
]
