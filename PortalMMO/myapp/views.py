from datetime import datetime
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .filters import AdvertisementFilter
from .forms import PostForm
from .models import Advertisement
from django.urls import reverse_lazy


class AdvertisementList(ListView):
    model = Advertisement
    ordering = '-some_datatime'
    template_name = 'flatpages/Advertisement.html'
    context_object_name = 'advertisement'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        return context


class AdvertisementDetail(DetailView):
    model = Advertisement
    template_name = 'flatpages/detail.html'
    context_object_name = 'detail'


class PostSearch(ListView):
    model = Advertisement
    ordering = '-some_datatime'
    template_name = 'flatpages/search.html'
    context_object_name = 'posts_search'
    paginate_by = 1

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdvertisementFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class AdvertisementCreate(CreateView):
    form_class = PostForm
    model = Advertisement
    template_name = 'flatpages/post_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user.username
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)


class AdvertisementUpdate(UpdateView):
    model = Advertisement
    form_class = PostForm
    template_name = 'flatpages/post_create.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Advertisement.objects.get(pk=id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = Advertisement.objects.get(pk=self.kwargs.get('pk')).author
        return context


class AdvertisementDelete(DeleteView):
    model = Advertisement
    template_name = 'flatpages/post_delete.html'
    success_url = reverse_lazy('advert_list')