# Generated by Django 2.2.14 on 2021-06-08 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0011_remove_orderitem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
    ]