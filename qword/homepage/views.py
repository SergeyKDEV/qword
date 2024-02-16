from django.views.generic import TemplateView


class HomePage(TemplateView):
    """Начальная страница."""
    template_name = 'homepage/index.html'


class AboutPage(TemplateView):
    """Информационная страница."""
    template_name = 'homepage/about.html'
