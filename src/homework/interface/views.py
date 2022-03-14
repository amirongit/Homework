from courseapp.models import Course
from django.views import generic

# Create your views here.


class Index(generic.ListView):
    template_name = 'interface/index.html'
    context_object_name = 'course_set'

    def get_queryset(self):
        return Course.objects.all().order_by('-id')[:6]

    def get_context_data(self, *args, **kwargs):
        cxt = super().get_context_data(*args, **kwargs)
        cxt.update({'title': 'Homepage'})
        return cxt
