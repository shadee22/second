# Generated by Django 2.2.14 on 2021-06-12 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0013_auto_20210612_0905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
