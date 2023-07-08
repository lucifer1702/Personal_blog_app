from django.db import models

# Create your models here.
class Post(models.Model):
   title=models.CharField(max_length=250)
   content=models.TextField()
   last_updated=models.DateTimeField(auto_now=True)
   slug=models.SlugField(unique=True, max_length=200)
   img=models.ImageField(null=True,blank=True,upload_to="images")
