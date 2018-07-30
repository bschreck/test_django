from django.views.generic import ListView
from .models import Company


class HomePageView(ListView):
    model = Company
    template_name = 'home.html'
