from django.urls import path
from loginApp import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout_views/', views.logout_views, name='logout_views'),
    path('not-found/', views.not_found_view, name='not_found'),
    # Other URL patterns
]
