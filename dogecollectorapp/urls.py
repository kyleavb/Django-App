from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:dog_id>/', views.show, name='show'),
    path('post_dog/', views.post_dog, name='post_dog'),
    path('user/<username>', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('like_dog/', views.like_dog, name='like_dog'),
    path('<int:dog_id>/edit/', views.edit_dog, name='edit_dog'),
    path('<int:dog_id>/delete/', views.delete_dog, name='delete_dog'),
    path('<int:dog_id>/toy/create/', views.create_toy, name='create_toy'),
    path('toy/<int:toy_id>/', views.show_toy, name='show_toy'),
    path('api/', views.api, name='api'),
]
