from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=64)#제목 64자
    writer = models.ForeignKey('dsuser.Dsuser', on_delete=models.CASCADE)
    image_address = models.CharField(max_length=600)#이미지주소
    contents = models.TextField()
    registered_dttm = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('tag.Tag')
  

    def __str__(self):
        return self.image_address

    class Meta:
        db_table = 'Djangostar_post'