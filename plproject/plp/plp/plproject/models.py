from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    meta = models.CharField(max_length=255)
    year = models.IntegerField()
    km = models.IntegerField()
    price = models.CharField(max_length=255)

    def __str__(self):
        # return self.name
        return '%s, %s, %i, %s, %s' % (self.name, self.meta, self.year, self.km, self.price)
    
