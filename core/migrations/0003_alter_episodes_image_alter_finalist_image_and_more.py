# Generated by Django 5.0 on 2023-12-17 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_finalist_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episodes',
            name='image',
            field=models.ImageField(null=True, upload_to='episodes_images/'),
        ),
        migrations.AlterField(
            model_name='finalist',
            name='image',
            field=models.ImageField(null=True, upload_to='finalist_images/'),
        ),
        migrations.AlterField(
            model_name='services',
            name='image',
            field=models.ImageField(null=True, upload_to='services_images/'),
        ),
    ]
