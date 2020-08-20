from django.db import models

class Organisations(models.Model):

    name = models.CharField(max_length=254)
    content = models.TextField()
    link = models.CharField(max_length=254)
    logo = models.CharField(max_length=254)
    position = models.IntegerField(default=1)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('position',)