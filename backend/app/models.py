from django.db import models
from datetime import datetime    




class Posts (models.Model):

    title = models.CharField(max_length=250)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, blank=True)



    def __str__(self):
        return self.title