from datetime import timedelta
from .models import Paper
from .serializers import PaperListSerializer, PaperDetailSerializer
from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination


class PaperListPagination(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'offset'


class PaperListView(ListAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperListSerializer
    pagination_class = PaperListPagination
    
    def get_queryset(self):
        param = self.request.GET.get('limit', None)
        papers = Paper.objects.all()
        if param is None:
            return papers
        else:
            return papers.filter(updated_at__gte=(timezone.now() - timedelta(days=1)))


class PaperDetailView(RetrieveAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperDetailSerializer