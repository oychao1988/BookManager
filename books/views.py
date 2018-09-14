from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from books.models import BookInfo
from books.serializers import BookInfoSerializer

class BooksInfoView(ViewSet):
    def list(self, requset):
        serializer = BookInfoSerializer(instance=BookInfo.objects.all(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookInfoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class BookInfoView(ViewSet):
    def retrieve(self, request, pk):
        serializer = BookInfoSerializer(instance=BookInfo.objects.get(id=pk))
        return Response(serializer.data)

    def update(self, request, pk):
        serializer = BookInfoSerializer(instance=BookInfo.objects.get(id=pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        book.delete()
        return Response(status=204)