# Generated by Django 3.2 on 2021-06-23 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210623_1948'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unittype',
            options={'verbose_name': 'Тип узла', 'verbose_name_plural': 'Типы узлов'},
        ),
    ]