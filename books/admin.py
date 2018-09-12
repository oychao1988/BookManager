from django.contrib import admin
from books.models import BookInfo, HeroInfo

# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)