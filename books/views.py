from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from books.models import BookInfo
from books.serializers import BookInfoSerializer

class BooksInfoView(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer