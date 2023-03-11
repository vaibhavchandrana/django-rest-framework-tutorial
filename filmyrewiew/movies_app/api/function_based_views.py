from movies_app.models import Movie
from movies_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET','POST'])
def Movie_list(request):
    if request.method=='GET':
        movies=Movie.objects.all()  #return query set
        serial=MovieSerializer(movies,many=True)
        return Response(serial.data)
    
    if request.method=='POST':
        serial=MovieSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)
    

@api_view(['GET','PUT','DELETE'])
def movie_detail(request,pk):
    if request.method=='GET':
        data=Movie.objects.get(pk=pk)
        serial=MovieSerializer(data)
        return Response(serial.data)
        
    if request.method=='PUT':
        one_movie=Movie.objects.get(pk=pk)
        serial=MovieSerializer(one_movie,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)

    if request.method=='DELETE':
        one_movie=Movie.objects.get(pk=pk)
        one_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



