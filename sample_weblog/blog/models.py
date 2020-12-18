from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=255, blank=False, null=True)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, blank=False)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    narahat = models.BooleanField(default=False) # :))))
