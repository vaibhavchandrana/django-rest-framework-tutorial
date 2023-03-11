from django.shortcuts import render
from .models import Movie
from django.http import JsonResponse
# Create your views here.


def Movie_list(request):
    movies=Movie.objects.all()  #return query set
    print(movies.values())       #return values in form of dict
    data=list(movies.values())
    res_data={'movies':data}      # dictionaries of list
    return JsonResponse(res_data)       # converting dict to json


def movie_detail(request,pk):
    data=Movie.objects.get(pk=pk)
    movie_data={'name':data.name,'desc':data.desc,
    'status':data.active}
    return JsonResponse(movie_data)