# Generated by Django 5.0 on 2023-12-19 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_post_icontyperedesocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='iconTypeRedeSocial',
            field=models.CharField(choices=[('github', 'Github'), ('insta', 'Instragram'), ('twitter', 'Twitter'), ('face', 'Facebook'), ('linkedln', 'Linkedln')], max_length=10),
        ),
    ]