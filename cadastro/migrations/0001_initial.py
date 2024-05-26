# Generated by Django 4.1.1 on 2023-04-17 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='Email principal')),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('dataUltimaAlteracao', models.DateTimeField(auto_now=True, null=True, verbose_name='Última alteração')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
