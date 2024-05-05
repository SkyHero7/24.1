from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_management.urls', namespace='users')),
    path('', include('courses.urls', namespace='courses')),
]
