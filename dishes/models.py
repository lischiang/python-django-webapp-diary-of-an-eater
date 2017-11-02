from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=140)
    place = models.CharField(max_length=140)
    date = models.DateTimeField()
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.name
