from django.contrib import admin
from .models import Post, Club, Detail, Status
# Register your models here.

admin.site.register(Post)
admin.site.register(Club)
admin.site.register(Detail)
admin.site.register(Status)