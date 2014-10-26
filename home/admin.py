from django.contrib import admin
from home.models import Comment
from django.db import connection

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['comment_id']}),
        ('OP ID', {'fields': ['op_id']}),
        ('Comment', {'fields' : ['comment_text']}),
    ]

admin.site.register(Comment, CommentAdmin)