from django.forms.models import BaseModelForm
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from .models import Blog, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from .forms import CommentForm
import uuid
# Create your views here.
class MyBlogs(LoginRequiredMixin, TemplateView):
    template_name = 'AppBlog/blogsMine.html'
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ('title', 'content', 'images')
    template_name = 'AppBlog/blogCreate.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        title = obj.title
        datetime = str(obj.publish)
        obj.slug = title.replace(' ', '-') + "-" + str(uuid.uuid4())
        obj.save()
        return HttpResponseRedirect(reverse('index'))
class BlogList(ListView):
    context_object_name = 'blogs'
    template_name = 'AppBlog/blogList.html'
    model = Blog
class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'AppBlog/blogEdit.html'
    fields = ('title', 'content', 'images')
    def get_success_url(self):
        return reverse_lazy('Appblog:details', kwargs={'slug':self.object.slug})
@login_required
def deleteBlog(self, pk):
    blog = Blog.objects.get(pk=pk)
    blog.delete()
    return HttpResponseRedirect(reverse('Appblog:myBlogs'))
def blogDetails(req, slug):
    blog = Blog.objects.get(slug=slug)
    form = CommentForm()
    if(req.method == 'POST'):
        form = CommentForm(req.POST)
        if(form.is_valid()):
            obj = form.save(commit=False)
            obj.user = req.user
            obj.blog = blog
            obj.save()
            return HttpResponseRedirect(reverse('Appblog:details', kwargs={'slug':blog.slug}))
    isliked = Like.objects.filter(blog=blog, user=req.user)
    if(isliked):
        liked = True
    else:
        liked = False
    return render(req, 'Appblog/blogDetails.html', context = {'blog':blog, 'liked':liked, 'form':form})
@login_required
def liked(req, pk):
    blog = Blog.objects.get(pk=pk)
    user =req.user
    liked = Like.objects.filter(blog=blog, user=user)
    if not liked:
        Like(blog=blog, user=user).save()
        return HttpResponseRedirect(reverse('Appblog:details', kwargs={'slug':blog.slug}))
@login_required
def unliked(req, pk):
    blog = Blog.objects.get(pk=pk)
    user =req.user
    liked = Like.objects.filter(blog=blog, user=user)
    liked.delete()
    return HttpResponseRedirect(reverse('Appblog:details', kwargs={'slug':blog.slug}))