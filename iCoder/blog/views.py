from django.shortcuts import render,HttpResponse
from blog.models import post

# Create your views here.
def bloghome(request):
    allposts=post.objects.all()
    context={'allPosts':allposts}
    return render(request,'blog/blogHome.html',context)
   


def blogpost(request,slug):
    Post=post.objects.filter(slug=slug).first()#post referenced error
    context = {'Post':Post}
    return render(request,'blog/blogpost.html',context)
   
    