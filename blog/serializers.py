from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True)
    class Meta:
        model = Article
        fields = ('id','title','content','tags','create_time','modify_time')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('name','url')

class WebSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebSite
        fields = '__all__'

class FeedBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = '__all__'