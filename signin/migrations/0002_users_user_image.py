# Generated by Django 5.0.7 on 2024-08-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='USER_image',
            field=models.ImageField(default=None, max_length=150, null=True, upload_to='user/'),
        ),
    ]
