from django.urls import path

from research.views import PublicDataListView

urlpatterns = [
    path('research', PublicDataListView.as_view()),
    # path('/<int:number>', PublicDataDetailView.as_view())
]