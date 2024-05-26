# Generated by Django 4.1.1 on 2023-09-16 03:32

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_perfil_cargo_alter_perfil_imagem'),
        ('siteCecane', '0002_quemrespondeu_dataaniversario'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDocumento',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Tipo de Documento',
                'verbose_name_plural': 'Tipos de Documentos',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=255, verbose_name='Nome do Documento:')),
                ('descricao', models.TextField(blank=True, max_length=500, null=True, verbose_name='Descrição do Documento')),
                ('arquivo', models.FileField(upload_to='repositorio/', verbose_name='Arquivo')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('dataAlteracao', models.DateTimeField(auto_now=True, verbose_name='Última Alteração')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('quemCadastrou', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastro.pessoa', verbose_name='Quem Cadastrou')),
                ('tipo', models.ForeignKey(help_text='Guias, Cartilhas, Manuais, Gestão AF', on_delete=django.db.models.deletion.PROTECT, to='siteCecane.tipodocumento', verbose_name='Tipo do Documento')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
                'ordering': ['dataCadastro', 'nome'],
            },
        ),
    ]
