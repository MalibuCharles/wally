import imp
from unicodedata import name
from django.urls import path
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),

]
