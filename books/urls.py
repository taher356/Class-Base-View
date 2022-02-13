from django.urls import path

from books.views import BookDetailView, IndexView, GenreView, AddBookView, BookEditView
app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('add/', AddBookView.as_view(), name='add'),
    path('g/<str:genre>', GenreView.as_view(), name='genre'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
    path('<slug:slug>/edit', BookEditView.as_view(), name='edit-detail'),
]
