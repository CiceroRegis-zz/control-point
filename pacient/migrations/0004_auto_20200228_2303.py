# Generated by Django 2.2.2 on 2020-02-29 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacient', '0003_remove_pacient_iswhatsapp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pacient',
            name='photo',
            field=models.FileField(blank=True, max_length=200, null=True, upload_to='photos'),
        ),
    ]