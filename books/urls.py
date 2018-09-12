from django.conf.urls import url
from books.views import BooksInfoView, BookInfoView

urlpatterns = [
    url(r'^books/$', BooksInfoView.as_view()),
    url(r'^books/(?P<pk>\d+)/$', BookInfoView.as_view())
]

from rest_framework.routers import DefaultRouter
# from books.views import BookInfoViewSet
# myRouter = DefaultRouter()
# myRouter.register(r'books', BookInfoViewSet, base_name='books')
#
# urlpatterns += myRouter.urls