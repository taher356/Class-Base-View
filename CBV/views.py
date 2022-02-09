from django.db.models import F
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import TemplateView, RedirectView
from .models import Post


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.get(id=1)
        return context


class PostPreLoadTaskView(RedirectView):
    pattern_name = 'CBV:single-post'

    def get_redirect_url(self, *args, **kwargs):
        post = Post.objects.filter(pk=kwargs['pk'])
        post.update(count=F('count') + 1)
        return super().get_redirect_url(*args, **kwargs)


class SinglePostView(TemplateView):
    template_name = 'ex2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        return context
