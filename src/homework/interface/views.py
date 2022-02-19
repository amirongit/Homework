from django.views import generic

# Create your views here.


class Index(generic.TemplateView):
    template_name = 'interface/index.html'

    def get_context_data(self):
        return {'title': 'Homework'}
