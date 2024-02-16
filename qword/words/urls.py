from django.urls import path

from . import views

app_name = 'words'


urlpatterns = [
    path('',  views.WordListView.as_view(), name='list'),
    path('add/',  views.words_add, name='add'),
    path('<int:pk>/delete/',  views.words_delete, name='delete'),
]
