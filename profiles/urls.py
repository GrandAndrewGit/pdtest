from django.urls import path
from .views import ProfilePage, ProfileListView, user_login, user_logout, UpdateProfile


urlpatterns = [
    path('', ProfileListView.as_view(), name='profiles-list'),
    path('profile/', ProfilePage, name='profile'),
    path('profile-edit/', UpdateProfile.as_view(), name='profile-edit'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]