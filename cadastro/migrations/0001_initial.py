# Generated by Django 5.0.6 on 2024-05-31 15:58

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
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeCompleto', models.CharField(max_length=255, verbose_name='Nome Completo')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('email', models.CharField(max_length=255, null=True, unique=True, verbose_name='Email principal')),
                ('contato', models.CharField(blank=True, default=None, help_text='Fone de contato com DDD (63) 98765-4321', max_length=255, null=True, verbose_name='Fone de contato')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('sexo', models.CharField(blank=True, choices=[(None, 'Ainda não verificado'), ('M', 'Masculino'), ('F', 'Feminino')], max_length=2, null=True, verbose_name='Sexo')),
                ('dataNascimento', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Data de Cadastro')),
                ('dataUltimaAlteracao', models.DateTimeField(auto_now=True, null=True, verbose_name='Última alteração')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
                'ordering': ['nomeCompleto', 'ativo'],
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome de Perfil')),
                ('cargo', models.CharField(blank=True, choices=[(None, 'Ainda não configurado'), ('1', 'Estagiário(a)'), ('2', 'Desenvolvedor'), ('3', 'Agente')], max_length=4, null=True, verbose_name='Cargo')),
                ('imagem', models.ImageField(blank=True, help_text='Imagem que será mostrada em seu Perfil', null=True, upload_to='perfil', verbose_name='Imagem de Perfil')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cadastro.pessoa', verbose_name='Pessoa')),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfis',
                'ordering': ['nome', 'cargo', 'ativo'],
            },
        ),
    ]
