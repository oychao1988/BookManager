from rest_framework import serializers
from books.models import BookInfo, HeroInfo

class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    btitle = serializers.CharField(max_length=20, label='书名', required=False)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(default=0, label='阅读量', required=False)
    bcomment = serializers.IntegerField(default=0, label='评论量', required=False)
    bimage = serializers.ImageField(allow_null=True, label='图片', required=False)
    is_delete = serializers.BooleanField(default=False, label='逻辑删除')
    heroinfo_set = serializers.StringRelatedField(read_only=True, many=True, label='英雄')

    def create(self, validated_data):
        return BookInfo.objects.create(
            btitle=validated_data.get('btitle'),
            bpub_date=validated_data.get('bpub_date')
        )

    def update(self, instance, validated_data):
        instance.btitle = validated_data.get('btitle', instance.btitle)
        instance.bpub_date = validated_data.get('bpub_date', instance.bpub_date)
        instance.bread = validated_data.get('bread', instance.bread)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.bimage = validated_data.get('bimage', instance.bimage)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()
        return instance

class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        (0, 'female'),
        (1, 'male')
    )
    hname = serializers.CharField(max_length=20, label='姓名', required=False)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, default=0, label='性别', required=False)
    hcomment = serializers.CharField(max_length=200, label='人物描述', required=False)
    is_delete = serializers.BooleanField(default=False, label='逻辑删除', required=False)
    hbook = serializers.PrimaryKeyRelatedField(queryset=BookInfo.objects.all(), label='图书', many=True)

    def create(self, validated_data):
        return HeroInfo.objects.create(
            hname=validated_data.get('hname'),
            hgender=validated_data.get('hgender'),
            hcomment=validated_data.get('hcomment')
        )

    def update(self, instance, validated_data):
        instance.hname = validated_data.get('hname', instance.hname)
        instance.hgender = validated_data.get('hgender', instance.hgender)
        instance.bcomment = validated_data.get('bcomment', instance.bcomment)
        instance.is_delete = validated_data.get('is_delete', instance.is_delete)
        instance.save()
        return instance