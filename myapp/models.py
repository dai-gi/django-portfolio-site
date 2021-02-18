from django.db import models

class Post(models.Model):
    image = models.ImageField('イメージ画像', upload_to='img', null=True, blank=True)
    title = models.CharField("タイトル", max_length=100)
    content = models.TextField("内容")
    url = models.URLField('URL', max_length=400, null=True, blank=True)

    def __str__(self):
        return self.title


class Icon(models.Model):
    image = models.ImageField('イメージ画像', upload_to='img', null=True, blank=True)
    name = models.CharField("タイトル", max_length=20)
    comment = models.TextField("内容")

    def __str__(self):
        return self.name

