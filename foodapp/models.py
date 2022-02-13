from django.db import models

# Create your models here.

class Food(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    price = models.FloatField()


    def __str__(self):
        return self.name



class Cart(models.Model):

    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    is_confirm = models.BooleanField(default=False)






