from django.contrib import admin
from django.urls import include, path

app_name = 'homepage'

urlpatterns = [
    path('', include('homepage.urls'), name='homepage'),
    path('words/', include('words.urls'), name='words'),
    path('admin/', admin.site.urls),
]
