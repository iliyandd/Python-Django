# Generated by Django 3.2.7 on 2021-12-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Notes', '0005_auto_20211223_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
