from django.urls import path
from .views import PaperListView, PaperDetailView


urlpatterns = [
    path('papers', PaperListView.as_view(), name='paper-list'),
    path('papers/<int:pk>', PaperDetailView.as_view(), name='paper-detail'),
]