# Generated by Django 2.2.14 on 2021-05-18 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_auto_20210518_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]