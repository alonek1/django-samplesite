from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'title':'post1',
        'author':'user1',
        'content':'This is1',
    },
    {
        'title':'post2',
        'author':'user2',
        'content':'This is2',
    }
]

context = {
        'posts': posts,
        'title': ' Home Page',
    }
def blog(request):
    return render(request, 'blog.html',  context)

def about(request):
    #todo: send title and context in different variables
    return render(request, 'about.html', {'title':' About page'})

