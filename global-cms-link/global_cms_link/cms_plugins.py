"""CMS Plugins

This module consist of the plugin neccessary for Link component
"""

from __future__ import unicode_literals

from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import FilLinkPluginModel


class FilLinkPlugin(CMSPluginBase):
    """FilLinkPlugin class

    Plugin class which handles Fil Link
    """

    model = FilLinkPluginModel
    name = _('FilLink')
    render_template = 'global_cms_link/link.html'

    def render(self, context, instance, placeholder):
        context = super(FilLinkPlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(FilLinkPlugin)
