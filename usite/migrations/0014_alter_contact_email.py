# Generated by Django 3.2.6 on 2022-03-05 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usite', '0013_alter_blogposts_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=122),
        ),
    ]
