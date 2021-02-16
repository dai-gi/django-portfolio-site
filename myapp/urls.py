from django.urls import path
from myapp import views

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('post/new/', views.CreatePostView.as_view(), name='post_new'),
]