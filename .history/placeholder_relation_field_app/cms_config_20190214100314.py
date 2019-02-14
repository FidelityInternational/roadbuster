from cms.app_base import CMSAppConfig

from .models import FancyPoll
from .views import detail_view



class Example1CMSAppConfig(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(FancyPoll, render_example_content)]
