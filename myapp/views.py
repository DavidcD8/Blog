from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from .forms import RegistrationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Profile
from .forms import ProfileForm
from .forms import CommentForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from taggit.models import Tag
from .models import Category

# all the views are defined here


@login_required
def home(request):
    query = request.GET.get('search', '')  # Get search query from URL
    posts_list = Post.objects.filter(author=request.user)  # Fetch user's posts
   
    if query:
        posts_list = posts_list.filter(title__icontains=query)  # Search by title

    paginator = Paginator(posts_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')  # Get the page number from the URL
    page_obj = paginator.get_page(page_number)  # Get the posts for the current page
   
    return render(request, 'myapp/home.html', {'page_obj': page_obj})

def about(request):
    return HttpResponse('This is the about Page.')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # Don't save to the database yet
            post.author = request.user  # Assign the logged-in user as the author
            post.save()  # Now save to the database
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'myapp/create_post.html', {'form': form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to edit this post.")
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})


@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        return HttpResponseForbidden("You are not allowed to delete this post.")
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'delete_post.html', {'post': post})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Fetch all comments related to the post
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'myapp/post_detail.html', {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    })


@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[pk]))



def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to home page
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)

    # Generate the URL for the profile picture
    if not profile.profile_picture:
        profile_picture_url = '/static/images/default-profile-picture.jpg'  # Default image
    else:
        profile_picture_url = profile.profile_picture.url  # Uploaded image

    return render(request, 'myapp/profile.html', {
        'form': form,
        'profile': profile,
        'profile_picture_url': profile_picture_url,
    })


def category_posts(request, category_id):
    category = get_object_or_404(Category, id=category_id)  # Check if category exists
    posts = Post.objects.filter(category=category)         # Get posts for this category
    
    return render(request, 'myapp/category_posts.html', {'category': category, 'posts': posts})


def tagged_posts(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tags__in=[tag])
    
    return render(request, 'myapp/tagged_posts.html', {'tag': tag, 'posts': posts})
