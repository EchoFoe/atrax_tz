# Generated by Django 5.0.1 on 2024-02-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumberrange',
            name='capacity',
            field=models.CharField(verbose_name='Емкость'),
        ),
    ]
