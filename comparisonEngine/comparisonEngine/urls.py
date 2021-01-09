from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('compare.urls')),
    path('admin/', admin.site.urls),
]
