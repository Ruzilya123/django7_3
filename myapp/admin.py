from django.contrib import admin
from .models import Post, Author, Publisher, Category

# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)