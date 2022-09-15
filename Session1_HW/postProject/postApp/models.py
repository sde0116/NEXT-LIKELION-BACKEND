from unicodedata import category
from django.db import models

# Create your models here.
#Post
class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  category = models.TextField()
  like = models.BooleanField(default=False)
  like_num = models.IntegerField(default=0)

  def __str__(self):
    return self.title

#Comment
class Comment(models.Model):
  post = models.ForeignKey(
    Post, related_name="comments", on_delete=models.CASCADE
    )
  content = models.TextField()

  def __str__(self):
    return self.content

#User
class User(models.Model):
  user_name = models.CharField(max_length=10)
  user_id = models.CharField(max_length=20)
  user_password = models.CharField(max_length=20)
  user_major = models.ForeignKey(
    "Major", related_name="major", on_delete=models.CASCADE
  )

  def __str__(self):
    return self.user_name

#Major
class Major(models.Model):
  first_major = models.TextField()
  second_major_type = models.TextField()
  second_major = models.TextField()