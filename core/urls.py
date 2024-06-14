from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.homepage, name="homepage"),
    path('text/recogi/', views.output_text, name="output"),
    path('computer/vision', views.voice_asistance, name="voice")
   
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
