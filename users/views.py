from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render

from posts.models import Post

from .forms import ProfileEditForm, SignUpForm
from .models import Profile


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(
                user=user,
                display_name=user.username,
            )
            login(request, user)
            return redirect('posts:home')
    else:
        form = SignUpForm()

    return render(request, 'users/signup.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = user.posts.filter(status=Post.Status.PUBLISHED).order_by('-published_at')
    return render(request, 'users/profile.html', {'profile': profile, 'posts': posts})


@login_required
def edit_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = ProfileEditForm(instance=profile)

    return render(request, 'users/profile_edit.html', {'form': form})