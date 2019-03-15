"""Models

This module consist of all the models necessary for Contact Us component
"""

from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from filer.fields.file import FilerFileField
from global_cms_link.models import FilLink


class ContactUsContainerPluginModel(CMSPlugin):
    """ContactUsContainerPluginModel class

    Model class which handles Contact Us Container plugin component
    """

    class Meta:
        verbose_name = 'Contact Us Container'
        verbose_name_plural = 'Contact Us Containers'

    bg_image = FilerFileField(on_delete=models.PROTECT, verbose_name=_('background image'), 
    blank=True, null=True)

    def __str__(self):
        return ''

    def copy_relations(self, old_instance):
        self.contact_us_items.all().delete()

        for item in old_instance.contact_us_items.all():
            item.pk = None
            item.parent_plugin = self
            item.save()


@python_2_unicode_compatible
class ContactUsItemModel(models.Model):
    """ContactUsItemModel class

    Model class which handles Contact Us Item
    """

    title = models.CharField(max_length=33)
    sub_title = models.CharField(max_length=35)
    phone = models.CharField(max_length=18)
    time = models.CharField(max_length=40)
    cta = models.ForeignKey(
        FilLink,
        related_name="+",
        on_delete=models.PROTECT,
        verbose_name=_('link'),
    blank=True, null=True)
    cta_text = models.CharField(max_length=20, blank=True, verbose_name=_('link text'))
    parent_plugin = models.ForeignKey(ContactUsContainerPluginModel, related_name="contact_us_items")

    class Meta:
        verbose_name = 'Contact Us Item'
        verbose_name_plural = 'Contact Us Items'

    def __str__(self):
        return self.title
