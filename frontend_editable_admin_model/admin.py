from django.contrib import admin
from django.conf.urls import url
from cms.admin.placeholderadmin import FrontendEditableAdminMixin

from .models import FancyPoll
from . import views

@admin.register(FancyPoll)
class FancyPollAdmin(admin.ModelAdmin):
    def get_urls(self):
        def _url(regex, fn, name, **kwargs):
            return url(regex, self.admin_site.admin_view(fn), kwargs=kwargs, name=name)

        url_patterns = [
            _url(r'^detail/(?P<pk>\d+)/$', views.detail_view, name='detail_view', ),
        ]
        return url_patterns + super(FancyPollAdmin, self).get_urls()