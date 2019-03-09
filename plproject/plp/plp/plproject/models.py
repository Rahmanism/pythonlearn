from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    km = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        # return self.name
        return '%s, %i, %s, %s' % (self.name, self.year, self.km, self.price)
    
