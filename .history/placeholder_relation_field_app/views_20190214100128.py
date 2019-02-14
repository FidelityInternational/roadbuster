from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

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


def detail_view(request, pk):
    context = {}
    
    if request.user.is_staff and request.toolbar:
        instance = get_object_or_404(FancyPoll, pk=pk)
        request.toolbar.set_object(instance)
    else:
        instance = get_object_or_404(FancyPoll, pk=pk, publish=True)
    
    context['instance'] = instance        
    
    return render(request, instance.template, context)



def render_example_content(request, example_content):
    return detail_view(request, example_content.pk)