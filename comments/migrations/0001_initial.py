# Generated by Django 5.0.7 on 2024-08-11 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ucomment', models.TextField(max_length=5000)),
                ('UPBslug', models.CharField(max_length=500)),
                ('Ucomment_image', models.ImageField(default=None, null=True, upload_to='comment/')),
                ('UPdate', models.DateField(auto_now=True)),
            ],
        ),
    ]
