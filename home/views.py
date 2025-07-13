from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    """
    View to render homepage
    """
    template_name = 'home/index.html'
