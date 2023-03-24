from django.conf import settings
from django.db import models
class Recipe(models.Model):
    'Generated Model'
    title = models.CharField(max_length=256,)
    instructions = models.TextField(null=True,blank=True,)
    prep_time = models.IntegerField(null=True,blank=True,)
    cook_time = models.IntegerField(null=True,blank=True,)
    chef = models.ForeignKey("users.User",on_delete=models.CASCADE,null=True,blank=True,related_name="recipe_chef",)
    created_at = models.DateTimeField(null=True,blank=True,)
