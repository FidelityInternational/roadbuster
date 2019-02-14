from django.db import models
from django.urls import reverse

from cms.models.fields import PlaceholderRelationField


class FancyPoll(models.Model):
    name = models.CharField(max_length=255)
    template = models.CharField(max_length=255, default='detail.html')
    placeholders = PlaceholderRelationField()
    placeholder = PlaceholderField('placeholder')
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('admin:detail_view', args=[self.pk])

    def get_template(self):
        return self.template
