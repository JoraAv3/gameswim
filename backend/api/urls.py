from django.urls import path
from .views import ProductListView, RegisterView, LoginView, UserProfileView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-profile/', UserProfileView.as_view(), name='user-profile'),
]
