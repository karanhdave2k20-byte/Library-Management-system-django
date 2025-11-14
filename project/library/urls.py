from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_page, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-book/', views.add_book, name='add_book'),
    path('edit-book/<int:id>/', views.edit_book, name='edit_book'),
    path('delete-book/<int:id>/', views.delete_book, name='delete_book'),
    path('profile/', views.profile, name='profile'),
    path('password-reset/', views.password_reset_page, name='password_reset'),
]
