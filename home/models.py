from django.db import models

from datetime import datetime

class Comment(models.Model):
    comment_id = models.IntegerField(default = 0, primary_key = True)
    op_id = models.IntegerField(default = 0)
    comment_text = models.CharField(max_length = 10000)
    author = models.CharField(max_length = 100, default = "Anonymous")
    #post_time = models.DateTimeField('date published')