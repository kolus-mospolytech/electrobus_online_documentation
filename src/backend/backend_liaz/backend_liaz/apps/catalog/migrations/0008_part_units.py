# Generated by Django 3.2 on 2021-06-22 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210623_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='units',
            field=models.ManyToManyField(related_name='_catalog_part_units_+', to='catalog.Part'),
        ),
    ]