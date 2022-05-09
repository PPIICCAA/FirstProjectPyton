from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('products/', views.products),
    path('costumer/', views.costumer),
    path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
    path(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    path(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    path(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]

