from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .forms import FilLinkForm
from .models import FilLink


class FilLinkAdminBase(admin.ModelAdmin):
    """FilLinkAdminBase class

    Base Admin class which controls the FilLink Admin
    """

    form = FilLinkForm
    fieldsets = [
        (None, {
            'fields': (
                'name',
                ('external_link', 'internal_link'),
                'file',
            )
        }),
        (_('FilLink settings'), {
            'classes': ('collapse',),
            'fields': (
                ('mailto', 'phone'),
                ('anchor', 'target'),
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'attributes',
            )
        }),
    ]
    search_fields = ['name']

    class Meta:
        abstract = True

class FilLinkAdmin(FilLinkAdminBase):
    """FilLinkAdmin class

    Admin class which controls the FilLink Admin
    """
    pass

admin.site.register(FilLink, FilLinkAdmin)
