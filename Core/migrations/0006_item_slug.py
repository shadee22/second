# Generated by Django 2.2.14 on 2021-06-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_auto_20210518_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
