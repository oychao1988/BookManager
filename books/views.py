import json

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from books.models import BookInfo
from books.serializers import BookInfoSerializer

# Create your views here.

# class BookInfoViewSet(ModelViewSet):
#     queryset = BookInfo.objects.all()
#     serializer_class = BookInfoSerializer


from django.views import View
from django.http import HttpResponse, JsonResponse


class BooksInfoView(View):
    def get(self, requset):
        books = BookInfo.objects.all()
        blist = []
        for book in books:
            data = {
                'id': book.id,
                'btitle': book.btitle,
                'bpub_date': book.bpub_date,
                'bread': book.bread,
                'bcomment': book.bcomment,
                'is_delete': book.is_delete,
            }
            blist.append(data)
        return JsonResponse(data=blist, safe=False)

    def post(self, request):
        json_byte = request.body
        json_str = json_byte.decode()
        book_dict = json.loads(json_str)
        book = BookInfo.objects.create(
            btitle = book_dict.get('btitle'),
            bpub_date = book_dict.get('bpub_date'),
        )
        return JsonResponse(data={
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date
        })

class BookInfoView(View):
    def get(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        return JsonResponse(data={
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment,
        })

    def put(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        json_byte = request.body
        json_str = json_byte.decode()
        book_dict = json.loads(json_str)

        book.btitle = book_dict.get('btitle', book.btitle)
        book.bpub_date = book_dict.get('bpub_date', book.bpub_date)
        book.save()

        return JsonResponse(data={
            'id': book.id,
            'btitle': book.btitle,
            'bpub_date': book.bpub_date,
            'bread': book.bread,
            'bcomment': book.bcomment
        })

    def delete(self, request, pk):
        book = BookInfo.objects.get(id=pk)
        book.delete()
        return HttpResponse(status=204)