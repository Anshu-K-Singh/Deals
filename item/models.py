from django.db import models
# here we will import the user to mention it in side the created  by field
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    class Meta:
        ordering = ("name",)
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name


class Item(models.Model):
    name= models.CharField(max_length=255)
    Category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE, default=1) #if category delete then all the items in category should delete
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image= models.ImageField(upload_to='item_images', null=True, blank=True)
    is_sold= models.BooleanField(default=False)
    created_at = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    
    #always make migrations after creating a new  model here
    
    def __str__(self):
        return self.name