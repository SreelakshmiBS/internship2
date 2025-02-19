
from django.shortcuts import render, redirect,get_object_or_404
from .models import * #model Post imported
from .forms import *  #form PostForm imported



def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts}) #see the posts you posted 

def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.word_count = len(post.content.split())  # Count words before saving
            post.save()
            return redirect('post_list') #create your post
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

def home(request):
    return render(request, 'myapp/home.html') #home page contains view and create post

def save(self, *args, **kwargs):
        self.word_count = len(self.content.split())  # Count words before saving
        super().save(*args, **kwargs)

def post_remove(request,post_id):
    post = get_object_or_404(Post,id=post_id)
    post.delete()
    return redirect('post_list') #removes the post

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.word_count = len(post.content.split())  # Recalculate word count
            post.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form, 'post': post})  #edit the post you posted

def post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_view.html', {'post': post}) #see your post
