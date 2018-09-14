from rest_framework.viewsets import ModelViewSet

from books.models import BookInfo
from books.serializers import BookInfoSerializer

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer