from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    path('product-list/', views.product_list, name='product_list'),
    path('search-products/', views.search_products, name='search_products'),
    path('register/', views.register, name='register'),
    path('search/', views.search_results, name='search_results'),
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('add/<int:product_id>/<str:product_name>/<str:product_price>/', views.add_to_cart, name='add_to_cart'),
]
