# Generated by Django 3.0.5 on 2020-08-07 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rex_app', '0005_auto_20200807_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userattribute',
            name='background_color',
            field=models.IntegerField(choices=[(1, '#212529'), (2, '#001442'), (3, '#00321b')]),
        ),
    ]
