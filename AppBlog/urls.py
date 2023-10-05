
from django.urls import path
from AppBlog import views
app_name = "Appblog"

urlpatterns = [
    path('myBlogs/', views.MyBlogs.as_view(), name="myBlogs"),
    path('create/', views.CreateBlog.as_view(), name="create"),
    path('list/', views.BlogList.as_view(), name="list"),
    path('edit/', views.UpdateBlog.as_view(), name="edit"),
    path('details/', views.blogDetails, name="details"),
    path('liked/', views.liked, name="liked"),
    path('unliked/', views.unliked, name="unliked"),
]