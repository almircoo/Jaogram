
# Create your posts views here.

#django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

#forms
from posts.forms import PostForm

#models
from posts.models import Post

#utilities
from datetime import datetime

posts = [
     {
       'title': 'Mont Blac',
       'user': {
            'name': 'Yesika Cortes',
            'picture': 'https://picsum.photos/60/60?image=1027'
       },
       'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
       'photo': 'https://picsum.photos/200/200?image=1036',
     },
     {
       'title': 'Via Lactea',
       'user': {
            'name': 'Jesus Almirco',
            'picture': 'https://picsum.photos/60/60?image=1005'
       },
       'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
       'photo': 'https://picsum.photos/200/200?image=903',
     },
     {
       'title': 'Nuevo Auditorio',
       'user': {
            'name': 'Valery Quispe',
            'picture': 'https://picsum.photos/60/60?image=883'
       },
       'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
       'photo': 'https://picsum.photos/200/200?image=1076',
     },

]

@login_required
def list_posts(request):
    #list existing posts
    return render(request, 'posts/feed.html', {'posts': posts})


@login_required
def create_post(request):
    #create new post views
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(
         request = request,
         template_name = 'posts/new.html',
         context = {
            'form': form,
            'user': request.user,
            'profile': request.user.profile,
         }
    )
