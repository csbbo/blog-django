from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = 'SHAOBO的博客后台管理'
admin.site.site_title = '后台管理'

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','create_time','modify_time')
    list_display_links = ('id','title')
    search_fields = ('title','create_time')
    list_filter = ('create_time', 'tags')
    filter_horizontal = ('tags',)
    fieldsets = (
        ['基本信息',{
            'fields':('title','content'),
        }],
        ['高级选项',{
            'classes': ('collapse',), #classes 说明它所在的部分的 CSS 格式。这里让 Advance 部分隐藏
            'fields': ('tags',),
        }]
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id','name','create_time')
    search_fields = ('name',)

@admin.register(Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ('id','name','create_time')

@admin.register(WebSite)
class WebSiteAdmin(admin.ModelAdmin):
    list_display = ('id','name','create_time')

@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('id','client_ip','message','create_time')
    list_display_links = ('id','message')
