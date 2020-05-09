from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.CharField(max_length=200, null=True, blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title