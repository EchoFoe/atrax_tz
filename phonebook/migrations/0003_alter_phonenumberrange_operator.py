# Generated by Django 5.0.1 on 2024-02-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phonebook', '0002_alter_phonenumberrange_capacity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumberrange',
            name='operator',
            field=models.CharField(max_length=200, verbose_name='Оператор'),
        ),
    ]
