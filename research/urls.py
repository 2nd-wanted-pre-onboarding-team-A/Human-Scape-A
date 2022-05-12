from django.urls import path

from research.views import PublicDataListView, PublicDataDetailView, UpdateDataListView

urlpatterns = [
    path('research', PublicDataListView.as_view()),
    path('research/<int:id>', PublicDataDetailView.as_view()),
    path('weekly', UpdateDataListView.as_view()),
]