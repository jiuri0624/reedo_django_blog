import markdown
from django.db import models
from django.utils.html import strip_tags
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')

    class Meta:
        verbose_name = u"文章类目"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name
        


class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='名称')

    class Meta:
        verbose_name = u"文章标签"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=40, verbose_name='标题')
    abstract = models.CharField(max_length=500, verbose_name='文章摘要', blank=True)
    body = models.TextField()
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User,  on_delete= models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
    
    def __str__(self):
        return self.title
    
    def increase_views(self):
        self.views+=1
        self.save(update_fields=['views'])
    
    def save(self, *args, **kwargs):
        if not self.abstract:
            md = markdown.Markdown(extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite'])
            self.abstract = strip_tags(md.convert(self.body))[:350]+'...'
        super(Article,self).save(*args, **kwargs)