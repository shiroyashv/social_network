from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User)
    slug = models.SlugField(max_length=32, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Subscription(models.Model):
    subscriber = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1
    VOTES = ((LIKE, 'Like'), (DISLIKE, 'Dislike'))

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTES)
    created_at = models.DateTimeField(auto_now_add=True)


# class Friend(models.Model):
#     STATUS_CHOICES = (
#         ('pending', 'Pending'),
#         ('accepted', 'Accepted'),
#     )
#     user1 = models.ForeignKey(User, related_name='user1', on_delete=models.CASCADE)
#     user2 = models.ForeignKey(User, related_name='user2', on_delete=models.CASCADE)
#     status = models.CharField(max_length=8, choices=STATUS_CHOICES, default='pending')
