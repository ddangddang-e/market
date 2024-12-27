from django.urls import path
from . import views  # views.py에서 필요한 함수나 클래스 임포트

urlpatterns = [
    path('list/', views.product_list, name='product_list'),
    path('detail/<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
]
path('<int:pk>/like/', views.toggle_like, name='toggle_like'),
