from django.shortcuts import render
from django.utils import timezone
from .models import Post#The dot before models means current directory or current application

# Create your views here.
"""def post_list(request):
    return render(request, 'blog/post_list.html', {})
"""
#request (everything we receive from the user via the Internet)
#the last parameter, {}, is a place in which we can add some things for the template to use.We need to give them names (we will stick to 'posts' right now). :) It should look like this: {'posts': posts}
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
