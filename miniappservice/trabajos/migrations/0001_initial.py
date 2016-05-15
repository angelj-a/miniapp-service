# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-11 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClaseEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Clase de Equipo',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Domicilio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=125)),
                ('ciudad', models.CharField(max_length=100)),
                ('provincia', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(blank=True, max_length=100, null=True)),
                ('modelo', models.CharField(blank=True, max_length=100, null=True)),
                ('codigo_identificador', models.CharField(max_length=100, null=True)),
                ('identificacion_alternativa', models.CharField(max_length=200, null=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajos.ClaseEquipo')),
            ],
        ),
        migrations.CreateModel(
            name='NumeroDeTelefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_de_linea', models.CharField(choices=[('celular', 'Celular'), ('fija', 'Fijo')], default='celular', max_length=20)),
                ('numero', models.CharField(max_length=20, verbose_name='Número')),
            ],
        ),
        migrations.CreateModel(
            name='Trabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_de_ingreso', models.DateTimeField(blank=True, null=True)),
                ('fecha_de_salida', models.DateTimeField(blank=True, null=True)),
                ('detalles', models.TextField(blank=True, max_length=512, null=True)),
                ('falla_segun_cliente', models.TextField(max_length=512)),
                ('falla_identificada_por_service', models.TextField(blank=True, max_length=512, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajos.Cliente')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trabajos.Equipo')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='domicilio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajos.Domicilio', verbose_name='Domicilio'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero_de_telefono',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trabajos.NumeroDeTelefono', verbose_name='Número de teléfono'),
        ),
    ]
