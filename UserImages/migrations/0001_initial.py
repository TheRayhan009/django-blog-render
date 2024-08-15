# Generated by Django 5.0.7 on 2024-08-12 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UPImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UPimage', models.ImageField(upload_to='images')),
                ('UPtitel', models.CharField(max_length=500)),
                ('Pdate', models.DateField(auto_now_add=True)),
                ('PUimage', models.CharField(max_length=200)),
                ('PUname', models.CharField(max_length=30)),
            ],
        ),
    ]
