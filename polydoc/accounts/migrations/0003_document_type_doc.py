# Generated by Django 3.0.3 on 2020-03-03 15:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('accounts', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='type_doc',
            field=models.CharField(choices=[('Cours', 'cours'), ('Tp', 'Tp'), ('Td', 'Td')], default='Cours',
                                   max_length=10),
        ),
    ]