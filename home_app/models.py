from django.db import models


class Poem(models.Model):
    poem = models.TextField(max_length=600, unique=True)
    who_said = models.CharField(max_length=30)
    poem_type = models.CharField(max_length=30, default="رباعی")

    def __str__(self):
        return self.poem[:30]


class Info(models.Model):
    address = models.TextField(max_length=100)
    number = models.CharField(max_length=13)
    email = models.EmailField(max_length=40)
    whatsapp = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)


class ProgrammingExperience(models.Model):
    title = models.CharField(max_length=30)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title


class OtherExperience(models.Model):
    title = models.CharField(max_length=30)
    percentage = models.IntegerField()

    def __str__(self):
        return self.title


class HomePageInfo(models.Model):
    occupation = models.CharField(max_length=60)
    company = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    # desktop_image = models.ImageField(upload_to="wallpaper", help_text="1920x1080")
    # mobile_image = models.ImageField(upload_to="wallpaper", help_text="640x1145")


class Message(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    number = models.CharField(max_length=10)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"
