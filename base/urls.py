from . import views
from django.urls import path

urlpatterns = [
    path('secret/', views.SecretCreateView.as_view(), name='create_secret'),
    path('secret/<str:hash>/', views.SecretRetrieveView.as_view(), name='retrieve_secret'),
]