from django.urls import path, include
from .views import PostPostAPIView, PostWeekListAPIView, PostMonthListAPIView, \
PostNewestListAPIView, PostPopularListAPIView

urlpatterns = [
    path('post/create/', PostPostAPIView.as_view()),
    path('post/week/', PostWeekListAPIView.as_view()),
    path('post/month/', PostMonthListAPIView.as_view()),
    path('post/newest/', PostNewestListAPIView.as_view()),
    path('post/popular/', PostPopularListAPIView.as_view()),
]
