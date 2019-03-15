from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from global_cms_link.models import FilLink
from global_cms_link.cms_plugins import FilLinkPlugin


class FilLinkPluginTests(TestCase):

    def setUp(self):
        self.link = FilLink(name='link1', external_link='/test/link1')
        self.link.save()
        self.placeholder = Placeholder.objects.create(slot='test')
        self.model_instance = add_plugin(
            self.placeholder,
            FilLinkPlugin,
            'en',
            link = self.link,
        )

    def __get_html(self, instance):
        request = RequestFactory()
        renderer = ContentRenderer(request=request)
        return renderer.render_plugin(instance, {'request': request})

    def test_fil_link_plugin(self):
        plugin_instance = self.model_instance.get_plugin_class_instance()
        context = plugin_instance.render({}, self.model_instance, None)
        self.assertIn('instance', context)
        self.assertTrue(hasattr(context['instance'],'link'))
        html = self.__get_html(self.model_instance)
        self.assertIn('a href="/test/link1"', html)

