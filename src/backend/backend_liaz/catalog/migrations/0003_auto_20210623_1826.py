# Generated by Django 3.2 on 2021-06-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_body_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='units',
            field=models.ManyToManyField(related_name='_catalog_unit_units_+', to='catalog.Unit', verbose_name='Связанные узлы'),
        ),
        migrations.DeleteModel(
            name='Body',
        ),
    ]
