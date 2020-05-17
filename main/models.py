from django.db import models

# Create your models here.

class Card(models.Model):
    Card_title = models.CharField(max_length=200)
    Card_content = models.TextField()
    Card_published = models.DateTimeField("date published")
    
    def __str__(self):
        return self.Card_title
