from django.db import models


class Author(models.Model):
    name = models.CharField('name', 'name', max_length=30)


class Publisher(models.Model):
    name = models.CharField('name', 'name', max_length=30)
    authors = models.ManyToManyField(Author)


class Category(models.Model):
    name = models.CharField('name', 'name', max_length=30)


class Post(models.Model):
    title = models.CharField("title", "title", max_length=100)
    content = models.CharField("content", "content", max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    url = models.CharField("url", "url", max_length=50)
