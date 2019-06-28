from django.db import models
# Reverse is a very handy utility function Django provides us to reference an object by
# its URL template name -- in this case post_detail.
from django.urls import reverse 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse('post_detail', args=[str(self.id)])