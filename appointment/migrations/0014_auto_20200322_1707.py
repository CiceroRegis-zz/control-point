# Generated by Django 2.2.2 on 2020-03-22 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0013_auto_20200322_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='typeappointment',
            name='name',
            field=models.TextField(max_length=200, verbose_name='Name'),
        ),
    ]
