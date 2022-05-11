from django.urls import path

from research.views import PublicDataListView, PublicDataDetailView

urlpatterns = [
    path('research', PublicDataListView.as_view()),
    path('research/<int:id>', PublicDataDetailView.as_view())
]