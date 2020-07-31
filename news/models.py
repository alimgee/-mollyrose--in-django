from django.db import models

class Article(models.Model):

    name = models.CharField(max_length=254)
    content = models.TextField()
    link = models.CharField(max_length=254)
    date = models.DateField()
    provider = models.CharField(max_length=254)


    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('date',)
