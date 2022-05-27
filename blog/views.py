from django.shortcuts import render
from .models import Post, Author
from .forms import PostForm
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    template_name = 'home.html'
    queryset = Post.objects.order_by('-updated_at')[:10]
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        p1 = Post.objects.get(slug=self.kwargs['slug']) 
        context['comment_list'] = p1.comment_set.all()
        return context


class AuthorListView(ListView):
    template_name = 'author_list.html'
    queryset = Author.objects.order_by('name')[:10]


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('blog:post_list')
