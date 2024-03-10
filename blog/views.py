from django.shortcuts import render, redirect, get_object_or_404
from taggit.models import Tag

from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import PostForm


def post_list(request):
    posts = Post.objects.all().order_by('id')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post_list.html',
                  {'posts': posts, 'page': page})


def post_detail(request, post_id):
    current_user = request.user
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post, 'current_user': current_user})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            form.save_m2m()
            return redirect('post_list')
        else:
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def post_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tagged_items__tag_id__in=[tag.id])
    return render(request, 'posts_by_tag.html', {'posts': posts, 'tag': tag})
