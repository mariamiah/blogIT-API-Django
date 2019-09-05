from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.urls import reverse
from .utils import unique_code_generator

# Create your models here.
class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    publish = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    
    class Meta:
        ordering = ('-publish',)
    
    def __str__(self):
        return self.title

def article_pre_save(sender, instance, *args, **kwargs):
    if instance.title and not instance.slug:
        instance.slug = slugify(instance.title) + "-" + unique_code_generator()
pre_save.connect(article_pre_save, sender=Article)

