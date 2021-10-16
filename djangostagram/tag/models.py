from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=16)#태그16자 제한
    registered_dttm = models.DateTimeField(auto_now_add=True)
  

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Djangostar_tag'