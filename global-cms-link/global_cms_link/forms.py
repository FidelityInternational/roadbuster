# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.utils.encoding import python_2_unicode_compatible

from .models import FilLink


@python_2_unicode_compatible
class FilLinkForm(forms.ModelForm):

    class Meta:
        model = FilLink
        fields = '__all__'

    def __str__(self):
        return self.name or str(self.pk)

    def __init__(self, *args, **kwargs):
        super(FilLinkForm, self).__init__(*args, **kwargs)
