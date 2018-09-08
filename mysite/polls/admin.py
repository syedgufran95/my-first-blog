# from django.contrib import admin
# from  .models import *
#
#
#
# admin.site.register(Question)
# admin.site.register(Choice)

from django.contrib import admin
from .models import Post

admin.site.register(Post)