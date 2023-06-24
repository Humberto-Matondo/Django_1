from django.shortcuts import render
from blog.data import posts 


# Create your views here.
def blog(request): 
    context =  {
        'text': 'ESTAMOS NO BLOG ACTUALIZANDO', 
        'posts': posts
    }
    return render(request, 'blog\home.html', context)

from django.http import Http404, HttpResponse

def post(request, post_id): 

    #isso servira para quando eu acessar o post que desejo n seja preciso 
    found_post = None
    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None: 
        raise Http404('POST N ENCONTRADO, N EXISTE PROVAVELMENTE')        
    

    context =  {
        'text': 'ESTOU EM UM DOS POSTS', 
        'post': found_post,
        'title': found_post['title'] + ' - ', #para aparecer o titulo do post no topo(como titulo do site)
    }
    return render(request, 'blog\post.html', context)