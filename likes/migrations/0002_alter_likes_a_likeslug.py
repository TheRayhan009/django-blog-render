# Generated by Django 5.0.7 on 2024-08-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='A_likeSlug',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
