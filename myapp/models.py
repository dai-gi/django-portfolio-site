from django.db import models

class Post(models.Model):
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("内容")

    def __str__(self):
        return self.title
