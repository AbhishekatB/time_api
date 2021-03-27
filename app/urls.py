from django.urls import path
from .views import GetNewsletter

urlpatterns = [
    path('', GetNewsletter.as_view())
]