from rest_framework import serializers
from books.models import BookInfo, HeroInfo

class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20, label='书名')
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(default=0, label='阅读量')
    bcomment = serializers.IntegerField(default=0, label='评论量')
    bimage = serializers.ImageField(allow_null=True, label='图片')
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True)


class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = serializers.CharField(max_length=20, label='姓名')
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, default=0, label='性别')
    hcomment = serializers.CharField(max_length=200, label='人物描述')
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    hbook = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all(), label='图书', many=True)
