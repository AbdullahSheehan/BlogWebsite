
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/', admin.site.urls),
    path('account/', include('AppLogin.urls')),
    path('blog/', include('AppBlog.urls')),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
