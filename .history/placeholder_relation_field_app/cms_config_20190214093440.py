


class Example1CMSAppConfig(CMSAppConfig):
    cms_enabled = True
    cms_toolbar_enabled_models = [(FancyPoll, render_example_content)]
