from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    artist = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True) 
    description = models.TextField()
    image = models.ImageField(upload_to='', null=True, blank=True, default='/default.jpg')
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", db_constraint=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category", default='django')

   
    def __str__(self):
        return self.name
