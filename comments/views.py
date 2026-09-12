from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from posts.models import Post

from .forms import CommentForm


@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()

    return redirect('posts:post_detail', post_id=post.id)