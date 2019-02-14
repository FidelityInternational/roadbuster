from django.http import Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from cms.toolbar.utils import get_toolbar_from_request

from .models import FancyPoll

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



def detail_frontend(request, example_content):
    return detail_view(request, example_content.pk)