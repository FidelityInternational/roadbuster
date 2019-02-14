from django.http import Http404
from django.shortcuts import render

from cms.toolbar.utils import get_toolbar_from_request

from .models import FancyPoll

def _base_detail(request, instance, template_name='detail.html',
                 item_name="char_1", template_string='',):
    context = {}
    context['instance'] = instance
    context['instance_class'] = instance.__class__()
    context['item_name'] = item_name
    if hasattr(request, 'toolbar'):
        request.toolbar.set_object(instance)
    if template_string:
        context = RequestContext(request=request, dict_=context)
        engine = Engine.get_default()
        template = engine.from_string(template_string)
        return HttpResponse(template.render(context))
    else:
        return render(request, template_name, context)


def list_view(request):
    context = {}
    context['examples'] = FancyPoll.objects.all()
    context['instance_class'] = FancyPoll
    return render(request, 'list.html', context)


def detail_view(request, pk, template_name='detail.html', item_name="char_1",
                template_string='',):
    if request.user.is_staff and request.toolbar:
        instance = FancyPoll.objects.get(pk=pk)
        request.toolbar.set_object(instance)
    else:
        instance = FancyPoll.objects.get(pk=pk, publish=True)
    return _base_detail(request, instance, template_name, item_name, template_string)


def render_example_content(request, example_content):
    return detail_view(request, example_content.pk)



def detail_view(request, poll_id):
    try:
        poll = FancyPoll.objects.get(pk=poll_id)
    except FancyPoll.DoesNotExist:
        raise Http404('Fancy Poll doesn\'t exist')

    toolbar = get_toolbar_from_request(request)
    toolbar.set_object(poll)
    return render(request, poll.template, {'poll': poll})
