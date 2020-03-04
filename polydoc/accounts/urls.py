from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('choice_register/', views.choice_register, name='choice_register'),
                  path('login/', views.user_login, name='user_login'),
                  path('logout/', views.logout, name='user_logout'),
                  path('register_eleve/', views.register_eleve, name='register_eleve'),
                  path('register_prof/', views.register_prof, name='register_prof'),
                  path('ged/', views.ged, name='ged'),
                  path('upload/', views.upload, name='upload'),
                  path('ged/<int:pk>/', views.delete_doc, name='delete'),
                  path('logout/', views.user_logout, name='logout'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
