from django.urls import path
from .views import forecast

urlpatterns = [
    path('', forecast, name='forecast')

]

