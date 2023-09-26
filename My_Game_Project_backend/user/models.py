from django.db import models


class User(models.Model):
    username = models.CharField("用户名", max_length=100)
    password = models.CharField("密码", max_length=20)
    email = models.EmailField('邮箱', default='defult@example.com')
    is_active = models.BooleanField('邮箱是否已经验证', default=True)
    avatar_url = models.CharField('用户头像路径', max_length=128, default='')
    avatar = models.FileField('用户头像', upload_to='', default='')

    class Meta:
        db_table = 'My_Game_Project_user'
