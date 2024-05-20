from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Category(models.Model):
    name_category = models.CharField(max_length=20, unique=True)
    subscribers = models.ManyToManyField(User, blank=True, null=True, related_name='categories')

    def __str__(self):
        return self.name_category


class Advertisement(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    text = RichTextField()
    some_datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.headline.title()}: {self.text[:20]}'

    def preview(self):
        return self.text[:124] + '...'


class Responses(models.Model):
    post = models.ForeignKey(Advertisement, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    some_datatime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
