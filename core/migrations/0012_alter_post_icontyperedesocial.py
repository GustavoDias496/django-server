# Generated by Django 5.0 on 2023-12-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_alter_post_icontyperedesocial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='iconTypeRedeSocial',
            field=models.CharField(choices=[('face', 'Facebook'), ('linkedln', 'Linkedln'), ('insta', 'Instragram'), ('twitter', 'Twitter'), ('github', 'Github')], max_length=10),
        ),
    ]
