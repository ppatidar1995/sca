from django.views.generic import TemplateView

class Home(TemplateView):
    template_name = "index.html"

home_view = Home.as_view()