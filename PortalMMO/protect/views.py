from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from myapp.models import Advertisement


class IndexView(TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_author'] = not Advertisement.objects.filter(author=self.request.user).exists()
        return context