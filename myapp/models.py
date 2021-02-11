from django.db import models

class Post(models.Model):
    image = models.ImageField('画像', upload_to='img', null=True, blank=True)
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("内容")

    def __str__(self):
        return self.title
