from django.urls import path, include

urlpatterns = [
    path('api/v1/', include('research.urls')),
    path('api/v1/', include('paper.urls')),
]
