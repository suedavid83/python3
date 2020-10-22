from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from principal import views

urlpatterns = [
    path('setIdioma/<slug:idioma>/', views.setIdioma, name="setIdioma"),
    path('', views.home, name="home")
]
