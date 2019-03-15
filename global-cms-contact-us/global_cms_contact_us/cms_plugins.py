"""CMS Plugins

This module consist of the plugin necessary for Contact Us component
"""

from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ContactUsContainerPluginModel, ContactUsItemModel


class ContactUsItemInline(admin.TabularInline):
    """ContactUsItemInline class

    Inline class which handles Contact Us Item records
    """

    model = ContactUsItemModel
    max_num = 1
    extra = 1


class ContactUsItemInline2(admin.TabularInline):
    """ContactUsItemInline class

    Inline class which handles Contact Us Item records
    """

    name = _('Contact Us Items 2')
    model = ContactUsItemModel
    max_num = 1
    extra = 1

class ContactUsPlugin(CMSPluginBase):
    """ContactUsPlugin class

    Plugin class which handles Contact Us component
    """

    model = ContactUsContainerPluginModel
    name = _('Contact Us')
    render_template = 'global_cms_contact_us/contact_us.html'
    inlines = [
        ContactUsItemInline,
        ContactUsItemInline2
    ]

    def render(self, context, instance, placeholder):
        context = super(ContactUsPlugin, self).render(context, instance, placeholder)
        card_items = instance.contact_us_items.all()
        has_another_card = len(card_items) > 1

        context.update({
            'card_items': card_items,
            'has_another_card': has_another_card,
        })
        return context


plugin_pool.register_plugin(ContactUsPlugin)
