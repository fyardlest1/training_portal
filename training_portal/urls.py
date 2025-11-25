
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# import views from accounts app
from accounts import views as accounts_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('academy/', include('academy.urls')),
    path('', include('home.urls')),
    
    # accounts app urls
    path('register/', accounts_views.register_view, name='register'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', accounts_views.logout_view, name='logout'),
    
]

if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
