# Generated by Django 2.2.2 on 2020-03-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0015_auto_20200307_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='medical_record_number',
            field=models.IntegerField(blank=True, default=6020772, editable=False, null=True, verbose_name='Medical record number'),
        ),
    ]