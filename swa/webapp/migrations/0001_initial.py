# Generated by Django 3.2.19 on 2023-06-03 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('idAdmin', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(default='contra123', max_length=120)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Universidad',
            fields=[
                ('idUniversidad', models.AutoField(primary_key=True, serialize=False)),
                ('anio_periodo', models.IntegerField()),
                ('nombreU', models.CharField(max_length=50)),
                ('numDesertados', models.IntegerField()),
                ('numGraduados', models.IntegerField()),
                ('numInscritos', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Estadistica',
            fields=[
                ('idEstadistica', models.AutoField(primary_key=True, serialize=False)),
                ('anio_dato', models.IntegerField()),
                ('tipoGrafico', models.CharField(max_length=25)),
                ('idAdmin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('idUniversidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.universidad')),
            ],
        ),
    ]
