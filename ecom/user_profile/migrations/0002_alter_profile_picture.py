# Generated by Django 4.2.3 on 2023-07-16 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='user_profile', verbose_name='picture'),
        ),
    ]
