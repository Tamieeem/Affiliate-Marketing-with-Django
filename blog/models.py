from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from rest_framework import serializers
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_listed = models.DateTimeField(default=timezone.now)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title




class PostSerializer(serializers.ModelSerializer):
    author_id = serializers.ReadOnlyField(source='author.username')
    author_profile_image = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

