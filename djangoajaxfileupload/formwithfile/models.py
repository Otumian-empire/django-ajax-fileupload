from django.db import models


class FileForm(models.Model):
    username = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    file = models.FileField(upload_to='files/')

    def __str__(self):
        return self.username
