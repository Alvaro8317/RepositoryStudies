from django.db import models


class Car(models.Model):
    title = models.TextField(max_length=100)
    year = models.TextField(max_length=4, null=True)

    def __str__(self):
        return f"Car {self.title} of {self.year}"


