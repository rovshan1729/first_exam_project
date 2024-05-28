from django.db import models
from django.contrib.auth import get_user_model
from utils.models import BaseModel

User = get_user_model()

class Tag(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(BaseModel):
    tags = models.ManyToManyField(Tag)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)

    content = models.TextField()
    image = models.ImageField(upload_to='posts/', null=True, blank=True)

    is_approved = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(BaseModel):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    content = models.TextField()

    def __str__(self):
        return self.content
