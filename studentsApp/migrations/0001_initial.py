# Generated by Django 5.0.3 on 2024-04-06 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0001_initial'),
        ('roomsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ism', models.CharField(max_length=255)),
                ('familiya', models.CharField(max_length=255)),
                ('otasi', models.CharField(blank=True, max_length=255, null=True)),
                ('jins', models.CharField(choices=[('erkak', 'erkak'), ('ayol', 'ayol')], max_length=10)),
                ('telefon_shaxsiy', models.CharField(max_length=13)),
                ('telefon_qoshimcha', models.CharField(blank=True, max_length=13, null=True)),
                ('kurs', models.PositiveSmallIntegerField()),
                ('guruh', models.CharField(max_length=10)),
                ('tutor', models.CharField(max_length=255)),
                ('manzil', models.CharField(max_length=255)),
                ('talim_turi', models.CharField(choices=[('kunduzgi', 'kunduzgi'), ('sirtqi', 'sirtqi')], max_length=255)),
                ('qarzdor', models.PositiveIntegerField(default=0)),
                ('haqdor', models.PositiveIntegerField(default=0)),
                ('fakultet', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.fakultet')),
                ('joy', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='roomsApp.joy')),
                ('tuman', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainApp.tuman')),
            ],
            options={
                'verbose_name': 'Talaba',
                'verbose_name_plural': 'Talabalar',
            },
        ),
    ]
