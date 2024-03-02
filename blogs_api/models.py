from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=150, null=False, blank=False)
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True, default='default.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, related_name="category", default=1)
    
    def __str__(self):
        return self.name
