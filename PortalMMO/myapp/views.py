from datetime import datetime

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Advertisement


class AdvertisementList(ListView):
    model = Advertisement
    ordering = '-some_datatime'
    template_name = 'flatpages/Advertisement.html'
    context_object_name = 'advertisement'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context