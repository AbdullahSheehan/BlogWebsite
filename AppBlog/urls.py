
from django.urls import path
from AppBlog import views
app_name = "Appblog"

urlpatterns = [
    path('myBlogs/', views.MyBlogs.as_view(), name="myBlogs"),
    path('create/', views.CreateBlog.as_view(), name="create"),
    path('list/', views.BlogList.as_view(), name="list"),
    path('edit/<int:pk>/', views.UpdateBlog.as_view(), name="edit"),
    path('delete/<int:pk>/', views.deleteBlog, name="delete"),
    path('details/<slug>/', views.blogDetails, name="details"),
    path('liked/<int:pk>/', views.liked, name="liked"),
    path('unliked/<int:pk>/', views.unliked, name="unliked"),
]