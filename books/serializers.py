from rest_framework import serializers
from books.models import BookInfo, HeroInfo

class BookInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInfo
        fields = '__all__'

class HeroInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        fields = '__all__'