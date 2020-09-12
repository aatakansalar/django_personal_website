
from django.contrib import admin
from django.urls import path,include
from post import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('posts/', include('post.urls'), name="posts"),
    path('projects/', include('project.urls')),
    path('user/', include('user.urls')),
    # path('about/', views.about, name='about')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()