from django.urls import path

from .views import url_create

app_name = "shorter"

urlpatterns = [
    path('', url_create, name = 'Url_short'),
]