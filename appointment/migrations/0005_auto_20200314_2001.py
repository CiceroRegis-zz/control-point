# Generated by Django 2.2.2 on 2020-03-14 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20200314_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='date_appointment',
            field=models.DateTimeField(verbose_name='date of appointment'),
        ),
    ]
