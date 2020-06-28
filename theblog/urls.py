
from django.urls import path
from .views import HomeView, ArticleDetailView, CV_View

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('home', HomeView.as_view(), name="home"),
    path('myCV', CV_View.as_view(), name="cv"),
    #path('cv', name='article-detail'),
]
