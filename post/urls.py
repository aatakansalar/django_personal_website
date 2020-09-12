from django.contrib import admin
from django.urls import path,include
from . import views

app_name = "post"

urlpatterns = [
    path('', views.posts, name='posts'),
    path('makepost/', views.makepost, name="makepost"),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('post/<int:id>', views.post, name="post"),
    path('update/<int:id>', views.updatePost, name="updatePost"),
    path('delete/<int:id>', views.deletePost, name="deletePost"),
    path('tags/<int:id>', views.tag_posts, name="tagposts")
]