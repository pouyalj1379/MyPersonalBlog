from django.db import models


class Template(models.Model):
    # created_date = models.CharField(max_length=50)
    title = models.CharField(max_length=50, unique=True)
    body = models.TextField(max_length=500)
    preview_body = models.TextField(max_length=50)
    image = models.ImageField(upload_to="templates_images")
    file = models.FileField(upload_to="Templates_files")

    # quote = models.TextField(max_length=500)
    # who_said = models.CharField(max_length=50)
    # occupation = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.title} - {self.body[0:30]}"