# Generated by Django 2.2.3 on 2022-10-20 06:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Procesos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrodeentrega',
            name='user_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]