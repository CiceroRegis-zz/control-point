# Generated by Django 2.2.2 on 2020-03-22 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0031_auto_20200322_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=3694838, editable=False, null=True, verbose_name='Medical record number'),
        ),
    ]
