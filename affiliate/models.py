from django.db import models
import uuid
from django.utils import timezone
from django.contrib.auth.models import User


class AffiliateLinks(models.Model):
    unique_id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    product = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='affiliate_links')
    clicks_count = models.PositiveIntegerField(default=0)
    date_listed = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


