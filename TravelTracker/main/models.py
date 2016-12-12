from django.db import models
from django.contrib.auth.models import User


# once added model, go to Django shell to migrate, then create objects
class Location(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    predators = models.CharField(max_length=100)
    num_restaurants = models.IntegerField()
    img_url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
