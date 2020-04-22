from django.urls import path
from .views import *

app_name = 'accounts'
urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),

]
