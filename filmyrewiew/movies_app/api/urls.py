from django.urls import path,include
from movies_app.api.views import WatchDetailAV,WatchListAV,StreamPlateformListAV,StreamDetailAV
from movies_app.api.views import ReviewList,ReviewDetail,ReviewCreate
urlpatterns = [
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('plateform/',StreamPlateformListAV.as_view(),name='movie-list'),
    path('<int:pk>',WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/<int:pk>',StreamDetailAV.as_view(),name='movie-detail'),
    #movieid/reviews
    path('<int:pk>/review',ReviewList.as_view(),name='movie-detail'),
    # review/revie-id
    path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail'),
    #movie-id/create-review
    path('<int:pk>/review-create',ReviewCreate.as_view(),name='review-detail'),
]
