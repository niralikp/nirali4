from app.models import Movie,Song
from django.http import HttpResponse
# Create your views here.

def create(request):
    b=Movie(actor="ankita", actor_movie="abc", genre="ninties")
    b.save()
    res='data created sucessfully'
    return HttpResponse(res)

def read(request):
   objects = Movie.objects.all()
   res="printing all the enteries in the DB: <br>"
   for elt in objects:
        res+=elt.actor+ " " +elt.actor_movie+ " " + elt.genre+ "<br>"
   return HttpResponse(res)

def delete(request):
    objects = Movie.objects.all()
    res = "<br> all enteries are deleted </br>"
    objects.delete()
    return HttpResponse(res)

def update(request):
   objects = Movie.objects.all()
   res="updating entry<br>"
   b=Movie.objects.get(actor="padiya")
   b.actor='nirali'
   b.save() 
   for elt in objects:
        res+=elt.actor+ " " +elt.actor_movie+ " " + elt.genre+ "<br>"
   return HttpResponse(res)