# Generated by Django 5.0 on 2023-12-24 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_post_icontyperedesocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='iconTypeRedeSocial',
            field=models.CharField(choices=[('linkedln', 'Linkedln'), ('insta', 'Instragram'), ('face', 'Facebook'), ('github', 'Github'), ('twitter', 'Twitter')], max_length=10),
        ),
    ]