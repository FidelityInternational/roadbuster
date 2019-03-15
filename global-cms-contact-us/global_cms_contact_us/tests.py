from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.test.client import RequestFactory

from cms.api import add_plugin
from cms.models import Placeholder
from cms.plugin_rendering import ContentRenderer

from filer.fields.file import File
from global_cms_link.models import FilLink
from global_cms_contact_us.cms_plugins import ContactUsPlugin, ContactUsItemInline
from global_cms_contact_us.models import ContactUsItemModel, ContactUsContainerPluginModel


class MockRequest:
    pass


class MockSuperUser:
    def has_perm(self, perm):
        return True


class ContactUsPluginTestss(TestCase):

    def setUp(self):
        self.placeholder = Placeholder.objects.create(slot='test')
        bgImage = File(name='test1.jpg')
        bgImage.save()
        self.model_instance = add_plugin(
            self.placeholder,
            ContactUsPlugin,
            'en',
            bg_image=bgImage,
        )
        self.inline_model_item = ContactUsItemInline(ContactUsContainerPluginModel, AdminSite())
        self.request = MockRequest()
        self.request.user = MockSuperUser()

    def __mock_contact_us_item_model(self, multiple=False):
        cta = FilLink(name='cta', external_link='/test/link1')
        cta.save()
        ContactUsItemModel.objects.create(
            title='Contact us item title',
            sub_title='Contact us item sub title',
            phone='00123123',
            time='from time to time',
            cta=cta,
            cta_text='cta text',
            parent_plugin=self.model_instance,
        )
        if multiple:
            ContactUsItemModel.objects.create(
                title='Contact us item title2',
                sub_title='Contact us item sub title2',
                phone='001231232',
                time='from time to time2',
                cta=cta,
                cta_text='cta text2',
                parent_plugin=self.model_instance,
            )

    def test_plugin_context_single_inline(self):
        plugin_instance = self.model_instance.get_plugin_class_instance()
        plugin_instance.inlines = []
        plugin_instance.inlines.append(self.inline_model_item)
        self.__mock_contact_us_item_model();
        context = plugin_instance.render({}, self.model_instance, None)
        instance = context['instance']
        self.assertIn('instance', context)
        self.assertIn('card_items', context)
        self.assertIn('has_another_card', context)
        self.assertTrue(hasattr(instance, 'bg_image'))
        self.assertEqual(len(context['card_items']), 1)
        self.assertFalse(context['has_another_card'])

    def test_plugin_context_multiple_inlines(self):
        plugin_instance = self.model_instance.get_plugin_class_instance()
        plugin_instance.inlines = []
        plugin_instance.inlines.append(self.inline_model_item)
        self.__mock_contact_us_item_model(True);
        context = plugin_instance.render({}, self.model_instance, None)
        instance = context['instance']
        self.assertIn('instance', context)
        self.assertIn('card_items', context)
        self.assertIn('has_another_card', context)
        self.assertTrue(hasattr(instance, 'bg_image'))
        self.assertGreater(len(context['card_items']), 1)
        self.assertTrue(context['has_another_card'])

    def test_plugin_html_single_inline(self):
        self.__mock_contact_us_item_model();
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(self.model_instance, {})
        self.assertRegexpMatches(html, r'Contact us item title')
        self.assertRegexpMatches(html, r'Contact us item sub title')
        self.assertRegexpMatches(html, r'00123123')
        self.assertRegexpMatches(html, r'from time to time')
        self.assertRegexpMatches(html, r'cta text')
        self.assertRegexpMatches(html, r'<span class="fil-icon fil-icon-arrow-r-light"></span>')

    def test_plugin_html_multiple_inlines(self):
        self.__mock_contact_us_item_model(True)
        renderer = ContentRenderer(request=RequestFactory())
        html = renderer.render_plugin(self.model_instance, {})
        self.assertRegexpMatches(html, r'Contact us item title') #from this line: test for the first item
        self.assertRegexpMatches(html, r'Contact us item sub title')
        self.assertRegexpMatches(html, r'00123123')
        self.assertRegexpMatches(html, r'from time to time')
        self.assertRegexpMatches(html, r'cta text')
        self.assertRegexpMatches(html, r'<span class="fil-icon fil-icon-arrow-r-light"></span>')
        self.assertRegexpMatches(html, r'fil-contact-us-card--second') #from this line: test for the second item
        self.assertRegexpMatches(html, r'Contact us item title2')
        self.assertRegexpMatches(html, r'Contact us item sub title2')
        self.assertRegexpMatches(html, r'001231232')
        self.assertRegexpMatches(html, r'from time to time2')
        self.assertRegexpMatches(html, r'cta text2')
        self.assertRegexpMatches(html, r'<span class="fil-icon fil-icon-arrow-r-light"></span>')

    def test_get_fieldsets(self):
        form = self.inline_model_item.get_formset(self.request).form
        self.assertEqual(form._meta.fields, ['title', 'sub_title', 'phone', 'time', 'cta', 'cta_text', 'parent_plugin'])
