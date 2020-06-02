from django.db import models

# Create your models here.
class Article(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title= models.CharField(max_length=400)
    text = models.TextField(max_length=1000000)


    def __str__(self):
        return self.title

    def short(self):
        return self.text[:100]