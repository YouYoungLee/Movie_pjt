from django.urls import path

from . import views

urlpatterns = [
    path('call/',views.callmovie),
    path('movielist/',views.movie_list),   
    path('gmovielist/',views.gmovie_list),    
    path('movie_detail/<int:movie_pk>/',views.movie_detail),
    path('gmovie_detail/<int:movie_pk>/',views.gmovie_detail),
    path('movie_detail/<int:movie_pk>/reviews/',views.create_review),
    path('reviews/<int:movie_pk>/',views.reviews),
    path('<int:movie_pk>/reviews/<int:review_pk>/update_delete/',views.reviews_update_delete),

]
