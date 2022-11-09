# Generated by Django 4.1.2 on 2022-11-09 05:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacoes',
            name='doador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pontoscoleta',
            name='telefone',
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
    ]
