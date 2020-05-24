from django.contrib import admin
#設定管理後台
from .models import Post

admin.site.register(Post)