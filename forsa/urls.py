
from django.contrib import admin
from django.urls import path
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include("devloper.urls")),
    path('auth/',include("human_resources.urls"))

    
]
