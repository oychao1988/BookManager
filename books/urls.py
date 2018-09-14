from django.conf.urls import url
from books.views import BooksInfoView

urlpatterns = [
    url(r'^books/$', BooksInfoView.as_view({'get': 'list', 'post': 'create'})),
    url(r'^books/(?P<pk>\d+)/$', BooksInfoView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]

from rest_framework.routers import DefaultRouter
# from books.views import BookInfoViewSet
# myRouter = DefaultRouter()
# myRouter.register(r'books', BookInfoViewSet, base_name='books')
#
# urlpatterns += myRouter.urls