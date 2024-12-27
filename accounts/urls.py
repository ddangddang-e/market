from django.urls import path
from .migrations import views  # views.py에서 필요한 함수나 클래스 임포트

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
path('<str:username>/', views.profile, name='profile'),

from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),  # 프로필 페이지 URL
]
