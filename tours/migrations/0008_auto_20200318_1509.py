# Generated by Django 3.0.1 on 2020-03-18 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0007_contactus_tel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='command',
            name='photo_employee',
            field=models.ImageField(upload_to='images_command/'),
        ),
        migrations.AlterField(
            model_name='travel',
            name='photo_main',
            field=models.ImageField(upload_to='images_travel/'),
        ),
    ]
