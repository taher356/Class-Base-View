from django.urls import path, include

from books.views import BookDetailView, IndexView
app_name = 'books'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:slug>/', BookDetailView.as_view(), name='book-detail'),
]
