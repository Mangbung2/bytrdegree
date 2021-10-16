# Generated by Django 3.2.7 on 2021-10-15 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20211015_1029'),
        ('dsuser', '0002_auto_20211015_1029'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={},
        ),
        migrations.AlterField(
            model_name='post',
            name='contents',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='image_address',
            field=models.CharField(max_length=600),
        ),
        migrations.AlterField(
            model_name='post',
            name='registered_dttm',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dsuser.dsuser'),
        ),
        migrations.AlterModelTable(
            name='post',
            table='Djangostar_post',
        ),
    ]
