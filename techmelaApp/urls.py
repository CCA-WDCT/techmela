from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.logIn, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logOut, name='logout'),
    path('like', views.handleLikes, name='like'),
    path('score', views.markScore, name='markScore'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)