from django.urls import path
from .views import home, citizen_login, citizen_register, citizen_panel,citizen_profile,citizen_pass,citizen_update,logout

app_name = 'citizen'

urlpatterns = [
    path('', home, name='index'),
    path('login/', citizen_login, name='citizen_login'),
    path('register/', citizen_register, name='citizen_register'),
    path('panel/', citizen_panel, name='citizen_panel'),
    path('profile/', citizen_profile, name='citizen_profile'),
    path('pass/', citizen_pass, name='citizen_pass'),
    path('citizen_update/', citizen_update, name='citizen_update'),
    path('logout/', logout, name='logout'),
    # Add other paths as needed
]
