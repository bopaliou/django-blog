from django.urls import path
from .views import home, article_detail  # Assuming you have an article_detail view

urlpatterns = [
    path('', home, name='home'),
    path('article/<int:pk>/', article_detail, name='article_detail'),  # Example for article detail view
    
]