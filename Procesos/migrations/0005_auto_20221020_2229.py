# Generated by Django 2.2.3 on 2022-10-21 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Procesos', '0004_auto_20221020_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registrodeentrega',
            old_name='user',
            new_name='name',
        ),
    ]
