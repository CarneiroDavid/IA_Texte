from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def current_datetime(request):
    template = loader.get_template("index.html")
    api_route = reverse('moderation')
    # return HttpResponse(template.render({}, request))
    context = {
        'api_route': api_route
    }
    return render(request,'index.html',context)