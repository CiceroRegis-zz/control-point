# Generated by Django 2.2.2 on 2020-03-22 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0031_auto_20200322_1642'),
        ('appointment', '0011_auto_20200322_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notificationpacient',
            name='pacient',
        ),
        migrations.AddField(
            model_name='notificationpacient',
            name='pacient',
            field=models.ManyToManyField(to='pacient.Pacient', verbose_name='Pacient'),
        ),
    ]
