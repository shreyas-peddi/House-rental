# Generated by Django 3.0.8 on 2020-11-28 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_system', '0003_auto_20170416_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
    ]
