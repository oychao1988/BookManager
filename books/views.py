from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response

from books.models import BookInfo
from books.serializers import BookInfoSerializer

class BooksInfoView(GenericViewSet):
    queryset = BookInfo.objects.all()
    serializer_class = BookInfoSerializer

    def list(self, requset):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk):
        serializer = self.get_serializer(instance=self.get_object())
        return Response(serializer.data)

    def update(self, request, pk):
        serializer = self.get_serializer(self.get_object(), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        book = self.get_object()
        book.delete()
        return Response(status=204)