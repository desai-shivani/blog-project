from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView,TemplateView,UpdateView
from .models import UserPost
from .forms import PostForm
# Create your views here.

class HomeView(ListView):
    model = UserPost
    template_name = 'blog_app/index.html'
    context_object_name="blog_entries"
    ordering = ['-date']
    paginate_by = 3
    #default context name is object

class PostView(DetailView):
    model = UserPost
    template_name = 'blog_app/post_detail.html'

class CreatePostView(CreateView):
    # redirect_field_name = '/'
    form_class = PostForm
    template_name = 'blog_app/create_post.html' 
    success_url = '/'

class AboutView(TemplateView):
    template_name='blog_app/about.html'

class UpdatePostView(UpdateView):
    template_name = 'blog_app/update_post.html'
    success_url ='/'
    form_class = PostForm
    model = UserPost

class DeletePostView(DeleteView):
    
    model = UserPost
    success_url = '/'
    template_name = 'blog_app/delete_account.html'


