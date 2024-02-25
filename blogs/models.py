from django.db import models

# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/images', null=True, blank=True)
    
    def __str__(self):
        return self.name
