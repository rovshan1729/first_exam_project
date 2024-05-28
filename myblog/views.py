from rest_framework import permissions
from .models import Post, Comment, Tag
from .serializers import PostSerializer, CommentSerializer, TagSerializer
from rest_framework import generics
import datetime


class PostPostAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostWeekListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        time_span = datetime.now() - datetime.timedelta(days=7)
        if self.request.user.is_staff:
            return Post.objects.all().order_by('-views')[:5]
        return Post.objects.filter(is_approved=True, created_at__lte=time_span).order_by('-views')[:5]
    

class PostMonthListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        time_span = datetime.now() - datetime.timedelta(days=7)
        if self.request.user.is_staff:
            return Post.objects.all().order_by('-views')[:5]
        return Post.objects.filter(is_approved=True, created_at__lte=time_span).order_by('-views')[:5]

class PostNewestListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all().order_by('-created_at')[:5]
        return Post.objects.filter(is_approved=True).order_by('-created_at')[:5]
    

class PostPopularListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all().order_by('-views')[:5]
        return Post.objects.filter(is_approved=True).order_by('-views')[:5]