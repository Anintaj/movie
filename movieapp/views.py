import movies as movies
from django.http import HttpResponse
from . models import movie
from django.shortcuts import render, redirect
from .forms import movieform

# Create your views here.
def index(request):
    mov=movie.objects.all()
    context={
        'movielist':mov
    }
    return render(request,"index.html",context)
def detail(request,movie_id):
    movi=movie.objects.get(id=movie_id)
    # return HttpResponse("This is %s :"%movie_id)
    return render (request,"detail.html",{'movie':movi})
def addmovie(request):
    if request.method=="POST":
        name=request.POST.get('name')
        year = request.POST.get('year')
        description=request.POST.get('description')
        genre = request.POST.get('genre')
        image = request.FILES['pic']
        moviee= movie(name=name,year=year,genre=genre,description=description,image=image)
        moviee.save()

    return render (request,"add.html")

def update(request,id):
    mo=movie.objects.get(id=id)
    form=movieform(request.POST or None, request.FILES,instance=mo)
    if form. is_valid():
        form.save()
        return redirect('/')
    return render (request,'edit.html' ,{'form':form,'movie':mo})

def delete(request,id):
    if request.method=='POST':
        mm = movie.objects.get(id=id)
        mm.delete()
        return redirect('/')
    return render(request,'delete.html')




