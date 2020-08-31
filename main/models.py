from django.db import models

class Notice(models.Model):

    title = models.CharField(max_length=254)
    content = models.TextField()
    link = models.CharField(max_length=254)
    link_title = models.CharField(max_length=254)
    show = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

