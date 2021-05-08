from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login(request):
    return render(request, 'login.html')
    
@login_required(login_url='/login')
def add_blog(request):
    context = {'form': BlogForm}
    try:
        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(user=user ,title=title, content=content, image=image)
            print("Blog oBjects", blog_obj)

    except Exception as e:
        print(e)    
    return  render(request, 'add_blog.html', context)
    
@login_required(login_url='/login')
def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

@login_required(login_url='/login')
def see_blog(request):
    context={}
    try:
        blog_objs = BlogModel.objects.filter(user=request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)

@login_required(login_url='/login')
def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()
    except Exception as e:
        print(e)

    return redirect('/see_blog/')

@login_required(login_url='/login')
def blog_update(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.get(slug=slug)
        
        if blog_obj.user != request.user:
            return redirect('/')

        initial_dict = {'content': blog_obj.content}
        form = BlogForm(initial=initial_dict)

        if request.method == "POST":
            form = BlogForm(request.POST)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']
            
            blog_obj = BlogModel.objects.create(user=user ,title=title, content=content, image=image)
            print("Blog oBjects", blog_obj)

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    return render(request, 'update_blog.html', context)    
 
def register(request):
    return  render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('/login')