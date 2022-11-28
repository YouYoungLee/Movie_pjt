from django.contrib import admin
from django.urls import include, path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',include('movies.urls')),
    path('api/v2/', include('accounts.urls')),
    path('api/v3/', include('community.urls')),
    path('api/v4/', include('chat.urls')),
    path('accounts/',include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
