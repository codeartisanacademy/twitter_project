from django.db import models
from django.contrib.auth.models import User
from model_utils.models import TimeStampedModel

# Create your models here.
class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()

