# Generated by Django 2.2.2 on 2020-03-14 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0020_auto_20200311_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=21286017, editable=False, null=True, verbose_name='Medical record number'),
        ),
    ]