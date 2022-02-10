from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

from books.models import Book


class IndexView(TemplateView):
    template_name = "book/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context


class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book-detail.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Book.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)
        context['now'] = timezone.now()
        return context
