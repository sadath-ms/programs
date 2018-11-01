from django.db import models

from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approve_comments=True)

    def get_absolute_url(self):
        return reverse("detail",kwrgs={'pk':self.pk})

    def __str__(self):
        return self.title


class Comments(models.Model):
    post=models.ForeignKey('mac.Post',related_name='comments')
    author=models.CharField(max_length=200)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    approve_comments = models.BooleanField(default=False)


    def approve(self):
        self.approve_comments=True
        self.save()

    def get_absolute_url(self):
        return reverse("list_view")

    def __str__(self):
        return self.text
