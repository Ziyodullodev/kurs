from django.db import models

# Create your models here.
class Kurs(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='media/kurs/')
    max_student = models.IntegerField()
    course_time = models.CharField(max_length=50)
    price = models.IntegerField()
    about = models.TextField()

    def __str__(self) -> str:
        return self.course_time

class Users(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    tgid = models.CharField(max_length=30)
    phone = models.IntegerField()
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


