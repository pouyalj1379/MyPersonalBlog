from django.db import models


class Story(models.Model):
    created_date = models.CharField(max_length=50)
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField(max_length=5000)
    preview_body = models.TextField(max_length=50)
    image = models.ImageField(upload_to="stories")

    quote = models.TextField(max_length=500, unique=True)
    who_said = models.CharField(max_length=50)
    occupation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.body[0:30]}"