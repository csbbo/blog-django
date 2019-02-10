from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题',max_length=20,unique=True,null=False)
    content = models.TextField('文章内容',unique=True,null=False)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    modify_time = models.DateTimeField('修改时间',auto_now=True)
    tags = models.ManyToManyField('Tag',verbose_name = '标签',related_name='articles',related_query_name='article')
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __unicode__(self):
        return self.title
    __str__ = __unicode__

class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('标签名',max_length=10,unique=True,null=False)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __unicode__(self):
        return self.name
    __str__ = __unicode__

class Friend(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名字',max_length=40,unique=True,null=False)
    url = models.URLField('链接',unique=True,null=False)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __unicode__(self):
        return self.name
    __str__ = __unicode__

class WebSite(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名字',max_length=40,unique=True,null=False)
    url = models.URLField('链接',unique=True,null=False)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = '网站'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __unicode__(self):
        return self.name
    __str__ = __unicode__

class FeedBack(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField('留言内容',unique=False,null=False)
    client_ip = models.CharField('IP',max_length=150,unique=False,null=True)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name
        ordering = ['-create_time']
    def __unicode__(self):
        return self.message
    __str__ = __unicode__