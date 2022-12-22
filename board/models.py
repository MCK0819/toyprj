import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.db import models
from user.models import User
from config import settings

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=20)
    # writer = models.CharField(max_length=30, default='',blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user_id")
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    boardLike = models.IntegerField(default=0)
    boardView = models.IntegerField(default=0)
    dateCreated = models.DateTimeField(auto_now_add=True)
    like_users = models.ManyToManyField(User, related_name='like_boards')

    def __str__(self):
        return self.title

    # 조회수 기능
    @property
    def update_counter(self):
        self.boardView = self.boardView + 1
        self.save()

    # 추천(좋아요) 기능
    # @property
    # def like_counter(self):
    #     self.boardLike = self.boardLike + 1
    #     self.save()

class Photo(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='images/',blank=True, null=True)

# 삭제요청이 들어오면 로컬에 있는 이미지도 삭제해주는 기능
@receiver(post_delete, sender=Photo)
def file_delete_action(sender, instance, **kwargs):
    instance.image.delete(False)

