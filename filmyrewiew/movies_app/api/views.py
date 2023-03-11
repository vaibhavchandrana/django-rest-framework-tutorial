from movies_app.models import WatchList,StreamingPlateform,Reviews
from movies_app.api.serializers import WatchListSerializer,StreamingPlateformSerializer,ReviewSerailizer
from movies_app.api.serializers import ReviewSerailizer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

class StreamPlateformListAV(APIView):
    def get(self,request):
        plateform=StreamingPlateform.objects.all()  #return query set
        serial=StreamingPlateformSerializer(plateform,many=True)
        return Response(serial.data)

    def post(self,request):
        serial=StreamingPlateformSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)


class StreamDetailAV(APIView):
    def get(self,request,pk):
        data=StreamingPlateform.objects.get(pk=pk)
        serial=StreamingPlateformSerializer(data)
        return Response(serial.data)
    
    def put(self,request,pk):
        one_movie=StreamingPlateform.objects.get(pk=pk)
        serial=StreamingPlateformSerializer(one_movie,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)
    
    def delete(self,request,pk):
        one_movie=StreamingPlateform.objects.get(pk=pk)
        one_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):
    def get(self,request):
        movies=WatchList.objects.all()  #return query set
        serial=WatchListSerializer(movies,many=True)
        return Response(serial.data)

    def post(self,request):
        serial=WatchListSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)


class WatchDetailAV(APIView):
    def get(self,request,pk):
        data=WatchList.objects.get(pk=pk)
        serial=WatchListSerializer(data)
        return Response(serial.data)
    
    def put(self,request,pk):
        one_movie=WatchList.objects.get(pk=pk)
        serial=WatchListSerializer(one_movie,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)
    
    def delete(self,request,pk):
        one_movie=WatchList.objects.get(pk=pk)
        one_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# this is generic views mixed with mixins

# class ReviewList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewSerailizer

#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)

#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset=Reviews.objects.all()
#     serializer_class=ReviewSerailizer

#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)

# this is concrete class view

class ReviewList(generics.ListAPIView):
    # queryset=Reviews.objects.all()
    serializer_class=ReviewSerailizer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Reviews.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Reviews.objects.all()
    serializer_class=ReviewSerailizer

class ReviewCreate(generics.CreateAPIView):
    serializer_class=ReviewSerailizer
    def get_queryset(self):
        return Reviews.objects.all()

    def perform_create(self, serializer):
        pk=self.kwargs['pk']
        movie=WatchList.objects.get(pk=pk)
        # code for checking thet user already post any review or not
        user=self.request.user
        review_queryset=Reviews.objects.filter(watchlist=movie,review_user=user)
        if review_queryset.exists():
            raise ValidationError("you have already reviewed")
        
        if movie.number_rating==0:
            movie.avg_rating=serializer.validated_data['rating']
        else:
            movie.avg_rating=(movie.avg_rating+serializer.validated_data['rating'])/2

        movie.number_rating= movie.number_rating + 1
        movie.save()
        serializer.save(watchlist=movie,review_user=user)