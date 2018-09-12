from rest_framework.routers import DefaultRouter
from books.views import BookInfoViewSet

urlpatterns = []

myRouter = DefaultRouter()
myRouter.register(r'books', BookInfoViewSet, base_name='books')

urlpatterns += myRouter.urls