# Generated by Django 4.1.1 on 2024-04-13 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteCecane', '0005_tipodocumento_tipo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tipoquestionario',
            options={'ordering': ['id', 'nome', 'dataCadastro'], 'verbose_name': 'Questionário', 'verbose_name_plural': 'Questionários'},
        ),
        migrations.CreateModel(
            name='OpcoesItemQuestionario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.TextField(max_length=2800, verbose_name='Resposta')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.itemquestionario', verbose_name='Pergunta do Questionario')),
            ],
            options={
                'verbose_name': 'Opção de Resposta',
                'verbose_name_plural': 'Opções de Respostas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ItemDependente',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.opcoesitemquestionario', verbose_name='Opção')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pergunta', to='siteCecane.itemquestionario', verbose_name='Pergunta Secundária')),
                ('perguntaChave', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='perguntaChave', to='siteCecane.itemquestionario', verbose_name='Pergunta Principal')),
            ],
            options={
                'verbose_name': 'Item Dependente',
                'verbose_name_plural': 'Itens Dependentes',
                'ordering': ['id'],
            },
        ),
    ]
