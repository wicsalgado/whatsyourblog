from functools import wraps

from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .forms import PostForm
from .models import Category, Post, Tag


def staff_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('posts:home')
        return view_func(request, *args, **kwargs)
    return wrapper


def home(request):
    posts = Post.objects.filter(status=Post.Status.PUBLISHED)

    query = request.GET.get('q', '').strip()
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    category_id = request.GET.get('categoria')
    if category_id:
        posts = posts.filter(category_id=category_id)

    tag_id = request.GET.get('tag')
    if tag_id:
        posts = posts.filter(tags__id=tag_id)

    posts = posts.order_by('-views_count', '-published_at').distinct()

    trending_tags = (
        Tag.objects.annotate(
            post_count=Count('posts', filter=Q(posts__status=Post.Status.PUBLISHED))
        )
        .filter(post_count__gt=0)
        .order_by('-post_count')[:10]
    )

    context = {
        'posts': posts,
        'categories': Category.objects.all(),
        'trending_tags': trending_tags,
        'query': query,
        'selected_category': int(category_id) if category_id else None,
        'selected_tag': int(tag_id) if tag_id else None,
    }
    return render(request, 'posts/home.html', context)


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

    if not post.can_be_edited():
        return redirect('posts:my_posts')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect('posts:my_posts')
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})

@login_required
def send_to_review(request, post_id):
    post = get_object_or_404(request.user.posts, id=post_id)

    if request.method == 'POST' and post.can_be_sent_to_review():
        post.status = Post.Status.IN_REVIEW
        post.save()

    return redirect('posts:my_posts')

@login_required
@staff_required
def editorial_list(request):
    posts = Post.objects.filter(status=Post.Status.IN_REVIEW).order_by('created_at')
    return render(request, 'posts/editorial_list.html', {'posts': posts})


@login_required
@staff_required
def editorial_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'posts/editorial_detail.html', {'post': post})


@login_required
@staff_required
def approve_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and post.status == Post.Status.IN_REVIEW:
        post.status = Post.Status.PUBLISHED
        post.published_at = timezone.now()
        post.save()

    return redirect('posts:editorial_list')


@login_required
@staff_required
def reject_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST' and post.status == Post.Status.IN_REVIEW:
        post.status = Post.Status.REJECTED
        post.save()

    return redirect('posts:editorial_list')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)

    Post.objects.filter(id=post.id).update(views_count=F('views_count') + 1)
    post.refresh_from_db(fields=['views_count'])

    comments = post.comments.all()
    comment_form = CommentForm()

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })