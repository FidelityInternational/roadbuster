from cms.app_base import CMSAppConfig

from .models import FancyPollContent
from .views import detail_frontend


class FancyPollCMSAppConfig(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(FancyPollContent, detail_frontend)]

    djangocms_versioning_enabled = False  # -- 1
    # versioning = [
    #     VersionableItem(   # -- 2
    #         content_model=PostContent,
    #         grouper_field_name='post',
    #         copy_function=default_copy,
    #         preview_url=get_preview_url
    #     ),
    # ]
    # versioning_add_to_confirmation_context = {
    #     'unpublish': [stories_about_intelligent_cats],
    # }