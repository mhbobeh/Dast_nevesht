from django.urls import path
from .views import PostListView, PostDetailView, AuthorListView, PostCreateView

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('create/', PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
