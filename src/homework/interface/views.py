import imp
from django.views import generic
from django.shortcuts import HttpResponse

# Create your views here.


class Index(generic.TemplateView):
    template_name = 'interface/index.html'
