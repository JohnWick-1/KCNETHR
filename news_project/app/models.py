from django.db import models
# Create your models here.

class News(models.Model):
    Id=models.AutoField(primary_key=True,)
    Date=models.DateField(auto_now=True)
    Title = models.CharField(max_length=255,unique=True)
    Details= models.TextField(unique=True)
    NewsFrom=models.CharField(max_length=40)
    URL=models.URLField()

    class Meta:
        db_table = 'news'
