# Generated by Django 2.2.8 on 2020-02-17 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0013_auto_20200217_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collaborator',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='User'),
            preserve_default=False,
        ),
    ]
