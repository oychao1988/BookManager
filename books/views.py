from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from books.serializers import BookInfoSerializer

# Create your views here.

class BookInfoViewSet(ModelViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer