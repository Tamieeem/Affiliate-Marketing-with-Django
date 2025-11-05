from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_listed = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
