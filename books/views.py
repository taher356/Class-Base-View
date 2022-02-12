from django.db.models import F
from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.views.generic import TemplateView, ListView, FormView
from django.views.generic.detail import DetailView

from books.forms import AddForm
from books.models import Book


class AddBookView(FormView):
    template_name = "book/add.html"
    form_class = AddForm
    success_url = '/books/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class IndexView(ListView):
    template_name = "book/home.html"
    model = Book
    context_object_name = 'books'
    # paginate our objects
    paginate_by = 4

    # with that it will show just two object from db
    '''def get_queryset(self):
        return Book.objects.all()[:2]'''


class GenreView(ListView):
    template_name = "book/home.html"
    model = Book
    context_object_name = 'books'
    paginate_by = 2

    def get_queryset(self, *args, **kwargs):
        return Book.objects.filter(genre__contains=self.kwargs.get('genre'))


'''class IndexView(TemplateView):
    template_name = "book/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all()
        return context'''


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
