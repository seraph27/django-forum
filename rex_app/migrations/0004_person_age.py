# Generated by Django 3.0.5 on 2020-05-08 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rex_app', '0003_auto_20200508_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
