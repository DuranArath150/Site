# Generated by Django 2.2.3 on 2022-10-21 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Procesos', '0003_registrodeentrega_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrodeentrega',
            name='user_name',
        ),
        migrations.AddField(
            model_name='registrodeentrega',
            name='user',
            field=models.CharField(default=1, max_length=32),
            preserve_default=False,
        ),
    ]
