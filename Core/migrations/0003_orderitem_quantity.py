# Generated by Django 2.2.14 on 2021-05-18 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0002_auto_20210518_0046'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
