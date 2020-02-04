from django.urls import path
from images.views import ImageCreateView

urlpatterns = [
    path('', ImageCreateView.as_view()),
]
