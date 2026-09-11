from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PostForm


def home(request):
    return render(request, 'posts/home.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()

            return redirect('posts:home')
    else:
        form = PostForm()

    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def my_posts(request):
    posts = request.user.posts.all()

    return render(request, 'posts/my_posts.html', {'posts': posts})

@login_required
def edit_post(request, post_id):
    post = get_object_or_404(request.user.posts, id=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:my_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})