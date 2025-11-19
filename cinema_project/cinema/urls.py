from django.urls import path
from .views import MovieListCreateView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    path('api/cinema/movies/', MovieListCreateView.as_view()),
    path('api/cinema/movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view()),
]
