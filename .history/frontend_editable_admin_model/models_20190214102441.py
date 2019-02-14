from django.db import models
from django.urls import reverse

from cms.models.fields import PlaceholderRelationField
from cms.models.fields import PlaceholderField


class FancyPoll(models.Model):
    name = models.CharField(max_length=255)


class FancyPollContent(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    template = models.CharField(max_length=255, default='detail.html')
    placeholders = PlaceholderRelationField()

    def get_absolute_url(self):
        return reverse('admin:detail_view', args=[self.pk])

    def get_template(self):
        return self.template

    def __str__(self):
        return self.name        
