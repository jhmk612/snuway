from django.db import models
from lend.models import Lender
from django.contrib.auth.models import User
# Create your models here.

class Comment(models.Model):
    post=models.ForeignKey(Lender)
    content=models.TextField()
    writer=models.ForeignKey(User)


    def __str__(self):
        return self.content
