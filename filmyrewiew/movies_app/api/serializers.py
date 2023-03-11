from rest_framework import serializers
from movies_app.models import WatchList,StreamingPlateform,Reviews
       
class ReviewSerailizer(serializers.ModelSerializer):
    review_user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Reviews
        # fields="__all__"
        exclude=('watchlist',)



class WatchListSerializer(serializers.ModelSerializer):
    movieReview=ReviewSerailizer(many=True,read_only=True)
    class Meta:
        model=WatchList
        fields="__all__"
        # fields=['name','desc']
        # exclude=['active']

class StreamingPlateformSerializer(serializers.ModelSerializer):
    WatchList=WatchListSerializer(many=True, read_only=True)

    class Meta:
        model=StreamingPlateform
        fields="__all__"
    