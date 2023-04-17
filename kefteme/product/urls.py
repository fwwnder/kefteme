from django.urls import path
from .views import ProductListView, ProductCreateView, ProductDetailView, ProductDeleteView, ProductUpdateView

urlpatterns = [
    path('', ProductListView.as_view(), name='blog-home'),
    path('create/', ProductCreateView.as_view(), name='create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]