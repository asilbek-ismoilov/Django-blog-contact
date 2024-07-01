from django.shortcuts import render
from .models import Blog, Contact
from django.contrib import messages

from django.http import HttpResponseRedirect
from django.urls import reverse


def home_view(request):
    return render(request,'home.html')

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name,email=email,content=content)
            new_contact.save()
            messages.success(request, "Sizning xabaringiz yuborildi!!!") 
            return HttpResponseRedirect(reverse('home-page'))
        except:
            pass

    return render(request,'contact.html')


def blog_view(request):
    blog = Blog.objects.all()
    context = {'blogs':blog}

    return render(request,'blog.html',context)

def blog_detail_view(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}

    return render(request,'publication.html',context)



# "{% url 'blog-detail' %}"