from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(65)])
    subject = models.CharField(max_length=30)

    def __dtr__(self):
        return f"{self.first_name} {self.last_name} {self.age} {self.subject}"
