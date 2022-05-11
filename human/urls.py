from django.urls import path, include

urlpatterns = [
    path('research', include('research.urls')),
]
