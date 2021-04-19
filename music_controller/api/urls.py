from django.urls import path
from .views import main, test

urlpatterns = [
    path('here', main),
    path('', test)
]
