import requests
from django.shortcuts import get_list_or_404, get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Global_Movie, Movie, Review
from .serializers import (MovieListSerializer, ReviewSerializer, ReviewsSerializer)

# Create your views here.
# PRESENT_URL = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=b10b0d059ae2804b6fe8d904c581e3f9&targetDt=20221114"
# listdata = requests.get(PRESENT_URL)
# resDatas = listdata.json().get('boxOfficeResult')

# print(resDatas.get('dailyBoxOfficeList')[0].get('movieNm'))
temp_list=[]
movieid_list=[]
movie_list=[]
globalid_list=[]
def callmovie(request):
    PRESENT_URL = f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20221122"
    listdata = requests.get(PRESENT_URL)
    resDatas = listdata.json().get('boxOfficeResult')
    for i in range(1,4):
        GLOBAL_URL = f"https://api.themoviedb.org/3/movie/now_playing?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR&page={i}"
        globalistdata = requests.get(GLOBAL_URL)
        globalresdatas = globalistdata.json().get('results')
        for i in range(20):
            globalid_list.append(globalresdatas[i].get('id'))
    for i in range(10):
        temp=resDatas.get('dailyBoxOfficeList')[i].get('movieNm')
        temp_list.append(temp)
    for i in temp_list:
        TMDB_URL=f"https://api.themoviedb.org/3/search/movie?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR&query={i}&page=1&include_adult=false"
        tmdblistdata = requests.get(TMDB_URL)
        tmdbresdatas = tmdblistdata.json().get('results')
        movieid_list.append(tmdbresdatas[0].get('id'))
    for i in movieid_list:
        try:
            temp_genre=[]
            actor_list=[]
            TMDBDETAIL_URL=f"https://api.themoviedb.org/3/movie/{i}?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
            tmdbdetaildata = requests.get(TMDBDETAIL_URL)
            title = tmdbdetaildata.json().get('title')
            release_data = tmdbdetaildata.json().get('release_date')
            vote_average = round(tmdbdetaildata.json().get('vote_average'),1)
            overview = tmdbdetaildata.json().get('overview')
            for j in range(len(tmdbdetaildata.json().get('genres'))):
                temp_genre.append((tmdbdetaildata.json().get('genres')[j].get('name')))
            genre = ', '.join(temp_genre)
            poster_path = tmdbdetaildata.json().get('poster_path')
            runnig_time = tmdbdetaildata.json().get('runtime')
            # print(title,release_data,vote_average,overview,genre,poster_path,runnig_time)
            TMDBCREDITS_URL=f"https://api.themoviedb.org/3/movie/{i}/credits?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
            tmdbcreditsdata = requests.get(TMDBCREDITS_URL)
            for k in range(5):
                actor_list.append(tmdbcreditsdata.json().get('cast')[k].get('name'))
            actor = ', '.join(actor_list)
            for l in range(20):
                if tmdbcreditsdata.json().get('crew')[l].get('job')=='Director':
                    director = tmdbcreditsdata.json().get('crew')[l].get('name')
                    break

            TMDBVIDEO_ULR=f'https://api.themoviedb.org/3/movie/{i}/videos?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko'
            tmdbvideodata = requests.get(TMDBVIDEO_ULR)
            try:
                video_temp = tmdbvideodata.json().get('results')[0].get('key')
            except IndexError:
                TMDBVIDEO_ULR=f'https://api.themoviedb.org/3/movie/{i}/videos?api_key=9dafc716aecd5cd988912f43b852ab6c&language=en'
                tmdbvideodata = requests.get(TMDBVIDEO_ULR)
                video_temp = tmdbvideodata.json().get('results')[0].get('key')
            video = ' https://www.youtube.com/embed/'+video_temp+'?autoplay=1&mute=1'
            movie = Movie(title=title,release_data=release_data,vote_average=vote_average,overview=overview,genre=genre,poster_path=poster_path,actor=actor,director=director,runnig_time=runnig_time,video=video)
            movie.save()
        except Exception:
            continue
    for i in globalid_list:
        try:
            temp_genre=[]
            actor_list=[]
            TMDBDETAIL_URL=f"https://api.themoviedb.org/3/movie/{i}?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
            tmdbdetaildata = requests.get(TMDBDETAIL_URL)
            title = tmdbdetaildata.json().get('title')
            release_data = tmdbdetaildata.json().get('release_date')
            vote_average = round(tmdbdetaildata.json().get('vote_average'),1)
            if tmdbdetaildata.json().get('overview')=="":
                continue
            else:
                overview = tmdbdetaildata.json().get('overview')
            for j in range(len(tmdbdetaildata.json().get('genres'))):
                temp_genre.append((tmdbdetaildata.json().get('genres')[j].get('name')))
            genre = ', '.join(temp_genre)
            poster_path = tmdbdetaildata.json().get('poster_path')
            runnig_time = tmdbdetaildata.json().get('runtime')
            # print(title,release_data,vote_average,overview,genre,poster_path,runnig_time)
            TMDBCREDITS_URL=f"https://api.themoviedb.org/3/movie/{i}/credits?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko-KR"
            tmdbcreditsdata = requests.get(TMDBCREDITS_URL)
            try:
                for k in range(5):
                    actor_list.append(tmdbcreditsdata.json().get('cast')[k].get('name'))
            except IndexError:
                pass
            actor = ', '.join(actor_list)
            for l in range(10):
                if tmdbcreditsdata.json().get('crew')[l].get('job')=='Director':
                    director = tmdbcreditsdata.json().get('crew')[l].get('name')
                    break

            TMDBVIDEO_ULR=f'https://api.themoviedb.org/3/movie/{i}/videos?api_key=9dafc716aecd5cd988912f43b852ab6c&language=ko'
            tmdbvideodata = requests.get(TMDBVIDEO_ULR)
            try:
                if tmdbvideodata:
                    video_temp = tmdbvideodata.json().get('results')[0].get('key')
                else:
                    TMDBVIDEO_ULR=f'https://api.themoviedb.org/3/movie/{i}/videos?api_key=9dafc716aecd5cd988912f43b852ab6c&language=en'
                    tmdbvideodata = requests.get(TMDBVIDEO_ULR)
                    video_temp = tmdbvideodata.json().get('results')[0].get('key')
            except IndexError:
                pass
            video = ' https://www.youtube.com/embed/'+video_temp+'?autoplay=1&mute=1'
            globalmovie = Global_Movie(title=title,release_data=release_data,vote_average=vote_average,overview=overview,genre=genre,poster_path=poster_path,actor=actor,director=director,runnig_time=runnig_time,video=video)
            globalmovie.save()
        except Exception:
            continue
     
    return Response('박스 오피스 불러오기 성공!!', status=status.HTTP_201_CREATED)

@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies,many=True)
        return Response(serializer.data)



@api_view(['GET'])
def gmovie_list(request):
    if request.method == 'GET':
        gmovies = get_list_or_404(Global_Movie)
        serializer = MovieListSerializer(gmovies,many=True)
        return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieListSerializer(movie)
    return Response(serializer.data)

@api_view(['GET'])
def gmovie_detail(request,movie_pk):
    gmovie = get_object_or_404(Global_Movie, pk=movie_pk)
    serializer = MovieListSerializer(gmovie)
    return Response(serializer.data)

@api_view(['POST'])
def create_review(request,movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user,movie=movie)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


@api_view(['GET'])
def reviews(request,movie_pk):
    reviews = get_list_or_404(Review,movie_id=movie_pk)

    if request.method == 'GET':
        serializer = ReviewsSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['PUT','DELETE'])
def reviews_update_delete(request,movie_pk,review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'PUT':
        review_serializer = ReviewSerializer(instance=review,data=request.data)
        if review_serializer.is_valid(raise_exception=True):
            review_serializer.save(movie=movie,user=request.user)
            return Response(review_serializer.data,status=status.HTTP_201_CREATED)

    else:
        review.delete()
        return Response(data='delete success',status=status.HTTP_204_NO_CONTENT)    
