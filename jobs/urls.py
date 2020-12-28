
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token # TOKEN

urlpatterns = [
    path('admin/', admin.site.urls), #  This is for Admin
    path('api/', include('jobs_api.urls')), # This is for API serializer
    path('auth/', obtain_auth_token), # This is for AUTH implemented TOKEN
]
