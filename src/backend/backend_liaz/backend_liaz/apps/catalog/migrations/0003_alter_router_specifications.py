# Generated by Django 3.2 on 2021-05-09 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_router'),
    ]

    operations = [
        migrations.AlterField(
            model_name='router',
            name='specifications',
            field=models.FileField(upload_to='uploads', verbose_name='Файл'),
        ),
    ]