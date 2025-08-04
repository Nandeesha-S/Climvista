from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('climate.urls')),  # root URL now maps to climate.urls

]
