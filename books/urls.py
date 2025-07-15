from django.urls import path
from .views import BookListCreateView, BookDetailView, ReadingListView, ReadingListDetailView, ReadingListItemView, RemoveBookFromReadingListView

urlpatterns = [
    path('', BookListCreateView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('reading-lists/', ReadingListView.as_view(), name='reading-list'),
    path('reading-lists/<int:pk>/', ReadingListDetailView.as_view(), name='reading-list-detail'),
    path('reading-lists/<int:pk>/add-book/', ReadingListItemView.as_view(), name='reading-list-add-book'),
    path('reading-lists/<int:list_pk>/remove-book/<int:book_pk>/', RemoveBookFromReadingListView.as_view(), name='reading-list-remove-book'),
]
