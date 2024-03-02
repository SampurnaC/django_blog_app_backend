from django.urls import path
from . import views

urlpatterns = [
    path('blog-list/', views.blogList, name='blog-list'),
    # path('blog-lists/', views.blogLists, name='blog-lists'),
    path('blog-detail/<str:pk>/', views.blogDetail, name='blog-detail'),
    path('blog-create/', views.blogCreate, name='blog-create'),
    path('blog-update/<str:pk>/', views.blogUpdate, name='blog-update'),
    path('blog-delete/<str:pk>/', views.blogDelete, name='blog-delete'),

    path('search/', views.blogSearch, name='search-blog'),


    path('category-lists/', views.categoryLists, name='category-lists'),

]
