from django.db import models

# Create your models here.

class Dsuser(models.Model):
    username = models.CharField(max_length=6)#아이디6자
    email = models.EmailField()
    password = models.CharField(max_length=24)#비밀번호24자
    registered_dttm = models.DateTimeField(auto_now_add=True)#가입시간 자동생성ㄴ

    def __str__(self):
        return self.username
    
    class Meta:
        db_table = 'Djangostar_dsuser'