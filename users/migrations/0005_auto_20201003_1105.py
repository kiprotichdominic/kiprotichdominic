# Generated by Django 2.2.7 on 2020-10-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200907_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(default='dommie.jpeg', upload_to='profile_pics'),
        ),
    ]
