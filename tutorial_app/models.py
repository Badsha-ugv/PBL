from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

COLOR = (
    ('dark', 'dark'),
    ('light', 'light'),
    ('primary', 'primary'),
    ('success','success'),
    ('info', 'info'),
    ('warning', 'warning'),
    ('danger', 'danger'),
)
class Category(models.Model):
    name = models.CharField(max_length=100)
    bg_color = models.CharField(max_length=10,choices=COLOR,blank=True,null=True)
    # slug = models.SlugField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
    class Meta:
        ordering = ['-created']
        verbose_name = 'Category-1'
        verbose_name_plural = 'Category-1'
    

class Topic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True) 
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.name}' 
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Topic-2'
        verbose_name_plural = 'Topic-2'

class Module(models.Model):
    # slug = models.SlugField(max_length=100, unique=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
    
    class Meta:
        ordering = ['created']
        verbose_name = 'Module-3'
        verbose_name_plural = 'Module-3'


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    body = RichTextUploadingField()

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        ordering = ['-created']
        verbose_name = 'Article-4'
        verbose_name_plural = 'Article-4'

