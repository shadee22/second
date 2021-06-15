# Generated by Django 2.2.14 on 2021-06-02 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0006_item_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='discription',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]