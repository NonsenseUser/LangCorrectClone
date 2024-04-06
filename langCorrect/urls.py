from django.urls import path, include
from . import views


urlpatterns = [
    path('journals/', views.journal, name='journal'),
    path('prompts/', views.prompts, name='prompts'),
    path('<str:post_title>/make_corrections/', views.corrections, name='corrections'),
    path('signup/', views.signup, name='signup'),
    path('journals/~create/', views.CreatePost.as_view(), name='creating_post'),
    path('journals/<str:pk>/', views.PostDetail.as_view(), name='post_detail'),

]
