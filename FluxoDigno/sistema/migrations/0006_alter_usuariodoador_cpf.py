# Generated by Django 4.1.2 on 2022-10-28 17:49

import django.core.validators
from django.db import migrations, models
import sistema.models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_alter_usuariodoador_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariodoador',
            name='cpf',
            field=models.CharField(max_length=11, unique=True, validators=[sistema.models.validacao_cpf, django.core.validators.MinLengthValidator(11)]),
        ),
    ]