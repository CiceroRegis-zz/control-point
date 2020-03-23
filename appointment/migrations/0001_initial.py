# Generated by Django 2.2.2 on 2020-03-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collaborator', '0003_auto_20200303_2158'),
        ('pacient', '0015_auto_20200307_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('skip', models.BooleanField(default=False, verbose_name='Skip')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Price of appointment')),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'typeAppointment',
                'verbose_name_plural': 'typeAppointment',
                'db_table': 'typeAppointment',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updateAt', models.DateTimeField(auto_now=True)),
                ('createAt', models.DateTimeField(auto_now_add=True)),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pacient.Pacient', verbose_name='Pacient')),
                ('professional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collaborator.Profile', verbose_name='Professional')),
                ('type_appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.TypeAppointment', verbose_name='Type appointment')),
            ],
            options={
                'verbose_name': 'appointment',
                'verbose_name_plural': 'appointment',
                'db_table': 'appointment',
            },
        ),
    ]