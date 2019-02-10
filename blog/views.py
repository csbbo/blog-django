from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *
from .send_emails import myblog_message

# Create your views here.

# https://q1mi.github.io/Django-REST-framework-documentation/
# https://www.django-rest-framework.org/
def test(request):
    return HttpResponse("This is the test page")

def index(request):
    return redirect('admin/')

class ArticleList(APIView):
    def get(self,request,format=None):
        if request.GET.get('id'):
            get_data = Article.objects.filter(id=request.GET.get('id'))
            serializer = ArticleSerializer(get_data,many=True)
            return Response(serializer.data)
        elif request.GET.get('tag'):
            get_data = Article.objects.filter(tags__name=request.GET.get('tag'))
            serializer = ArticleSerializer(get_data,many=True)
            return Response(serializer.data)
        elif request.GET.get('search'):
            get_data = Article.objects.filter(Q(title__contains=request.GET.get('search'))|
                Q(content__contains=request.GET.get('search')))
            serializer = ArticleSerializer(get_data,many=True)
            return Response(serializer.data)
        elif request.GET.get('page'):
            page_num = request.GET.get('page')
            get_data = Article.objects.all()
            serializer = ArticleSerializer(get_data,many=True)
            p = Paginator(serializer.data,10)
            current_page = p.page(page_num)
            p_dict = {
                'count':p.count,
                'num_pages':p.num_pages,
                'article':current_page.object_list,
                'article_num':current_page.number,
                'has_previous':current_page.has_previous(),
                'has_next':current_page.has_next()
            }
            return Response(p_dict)
        else:
            get_data = Article.objects.all()
            serializer = ArticleSerializer(get_data,many=True)
            return Response(serializer.data)
            

class TagList(APIView):
    def get(self,request,format=None):
        get_data = Tag.objects.all()
        serializer = TagSerializer(get_data,many=True)
        return Response(serializer.data)

class FriendList(APIView):
    def get(self,request,format=None):
        get_data = Friend.objects.all()
        serializer = FriendSerializer(get_data,many=True)
        return Response(serializer.data)

class WebSiteList(APIView):
    def get(self,request,format=None):
        get_data = WebSite.objects.all()
        serializer = WebSiteSerializer(get_data,many=True)
        return Response(serializer.data)

class FeedBackList(APIView):
    def post(self,request,format=None):
        if request.META.get('HTTP_X_FORWARDED_FOR'):
            ip =  request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        data = request.data.copy()
        data['client_ip'] = ip
        serializer = FeedBackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            myblog_message(serializer.data)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)