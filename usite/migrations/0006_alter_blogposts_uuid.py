# Generated by Django 3.2.6 on 2022-03-03 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usite', '0005_alter_blogposts_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogposts',
            name='uuid',
            field=models.AutoField(editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
