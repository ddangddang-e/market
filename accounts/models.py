from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # 추가 필드 정의 (필요한 경우)
    pass

    # groups와 user_permissions을 커스터마이즈
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='accounts_user_set',  # 기본 'user_set' 대신 사용
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='accounts_user_permissions',  # 기본 'user_permissions' 대신 사용
        blank=True
    )

    # 팔로우/팔로잉 관계를 위한 ManyToManyField
    followers = models.ManyToManyField(
        'self',  # 자기 자신을 참조
        symmetrical=False,  # 쌍방향 관계가 아닌 일방향 관계
        related_name='following',  # following 이름 지정
        blank=True,
        through='UserFollower'  # 중간 모델 지정
    )

# 중간 모델 (UserFollower) 정의
class UserFollower(models.Model):
    follower = models.ForeignKey(User, related_name='user_followers', on_delete=models.CASCADE)
    followed = models.ForeignKey(User, related_name='user_followed', on_delete=models.CASCADE)

    class Meta:
        # 중복된 팔로우 관계를 방지 (팔로우와 팔로잉 관계는 하나만 존재해야 함)
        unique_together = ('follower', 'followed')
