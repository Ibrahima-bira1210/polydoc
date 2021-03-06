# Generated by Django 3.0.3 on 2020-02-29 09:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id_classe', models.AutoField(primary_key=True, serialize=False)),
                ('nom_classe', models.CharField(
                    choices=[('TC1', 'TC1'), ('TC2', 'TC2'), ('DIC1-GC', 'DIC1-GC'), ('DIC1-GEM', 'DIC1-GEM'),
                             ('DIC1-GIT', 'DIC1-GIT'), ('DIC1-AERO', 'DIC1-AERO'), ('DIC2-GC', 'DIC2-GC'),
                             ('DIC2-GEM', 'DIC2-GEM'), ('DIC2-GIT', 'DIC2-GIT'), ('DIC2-AERO', 'DIC2-AERO'),
                             ('DIC3-GC', 'DIC3-GC'), ('DIC3-GEM', 'DIC3-GEM'), ('DIC3-GIT', 'DIC3-GIT'),
                             ('DIC3-AERO', 'DIC3-AERO')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mat_ens', models.CharField(max_length=200)),
                ('bio', models.TextField(default='ma bio', max_length=100)),
                ('photo_p', models.ImageField(default=None, upload_to='upload')),
                ('prof_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_matiere', models.AutoField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=200)),
                ('id_classe',
                 models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Classe')),
            ],
        ),
        migrations.CreateModel(
            name='Enseigner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_matiere',
                 models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Matiere')),
                ('id_prof',
                 models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.Prof')),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(default='ma bio', max_length=100)),
                ('photo_e', models.ImageField(default=None, upload_to='upload')),
                ('class_eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Classe')),
                ('eleve_user',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
