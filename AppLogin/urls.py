
from django.urls import path
from AppLogin import views
app_name = "Applogin"

urlpatterns = [
    path('register/', views.registerUser, name="register"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('profile/', views.profileUser, name="profile"),
    path('editProfile/', views.editProfile, name="editProfile"),
    path('addPicture/', views.addPicture, name="addPicture"),
    path('changePicture', views.changePicture, name="changePicture"),
    path('passwordChange', views.passwordChange, name="passwordChange"),
]