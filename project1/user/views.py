from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User




# def home(request):
#     content = {
#         "posts": Post.objects.all()
#         }
#     return render(request, 'user/home.html',content)

class PostListView(ListView):
    model=Post
    template_name= "user/home.html"
    context_object_name= "posted"
    ordering= ['date_posted']
    paginate_by= 3

class UserPostListView(ListView):
    model=Post
    template_name= "user/userpost.html"
    context_object_name= "posted"
    paginate_by= 3

    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    

class PostDetailView(DetailView):
    model=Post
    template_name="user/post_detail.html"

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=Post
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True

    def get_success_url(self) -> str:
        return '/'
        
         


def about(request):
    return render(request, 'user/about.html')