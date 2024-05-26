# Generated by Django 4.1.1 on 2023-09-12 03:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AGF', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemQuestionario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.IntegerField(blank=True, choices=[(0, 'Escolha'), (1, 'Multipla Escolha'), (2, 'Texto')], default=0, null=True, verbose_name='Tipos de questão')),
                ('descricao', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Descrição do Item do Questionário')),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Item do Questionário',
                'verbose_name_plural': 'Itens do Questionário',
                'ordering': ['id', 'ativo'],
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField(max_length=255, verbose_name='Título da Notícia:')),
                ('img', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Imagem da Notícia')),
                ('subtitulo', models.TextField(blank=True, max_length=280, null=True, verbose_name='Subtítulo da Notícia')),
                ('noticia', models.TextField(verbose_name='Corpo da Notícia')),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('dataAlteracao', models.DateTimeField(auto_now=True, verbose_name='Última Alteração')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='QuemRespondeu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=100, verbose_name='Nome')),
                ('sobrenome', models.TextField(max_length=100, verbose_name='Sobrenome')),
                ('telefone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('cidade', models.TextField(max_length=100, verbose_name='Cidade')),
                ('cargo', models.TextField(max_length=100, verbose_name='Cargo')),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Quem Respondeu',
                'verbose_name_plural': 'Quem Respondeu',
                'ordering': ['id', 'ativo'],
            },
        ),
        migrations.CreateModel(
            name='Slideshow',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('titulo', models.TextField(max_length=255, verbose_name='Título do Slide')),
                ('subtitulo', models.TextField(blank=True, max_length=280, null=True, verbose_name='Subtítulo do Slide')),
                ('img', models.ImageField(upload_to='images/slideshow', verbose_name='Imagem do Slide')),
                ('ativo', models.BooleanField(default=True, editable=False, verbose_name='Ativo?')),
            ],
            options={
                'verbose_name': 'Slideshow',
                'verbose_name_plural': 'Slideshow',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TipoQuestionario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255, verbose_name='Nome do Questionário:')),
                ('descricao', models.TextField(blank=True, max_length=280, null=True, verbose_name='Descrição do Questionário')),
                ('tipoDoQuestionario', models.IntegerField(blank=True, choices=[(0, 'Escolar'), (1, 'CAE'), (2, 'Agricultores'), (3, 'Gestão AF')], default=0, null=True, verbose_name='Tipos de questionário')),
                ('slug', models.SlugField(blank=True, max_length=150, unique=True, verbose_name='Slug')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('dataAlteracao', models.DateTimeField(auto_now=True, verbose_name='Última Alteração')),
                ('quemCadastrou', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Quem Cadastrou')),
            ],
            options={
                'verbose_name': 'Tipo de Questionário',
                'verbose_name_plural': 'Tipos de Questionários',
                'ordering': ['id', 'nome', 'dataCadastro'],
            },
        ),
        migrations.CreateModel(
            name='RespostasQuestionario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.IntegerField(choices=[(0, 'Não'), (1, 'Sim'), (2, 'Não se aplica')], default=1, verbose_name='Valores que podem ser selecionados')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='AGF.escola', verbose_name='Escola')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.itemquestionario', verbose_name='Pergunta do Questionario')),
                ('quemCadastrou', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Quem Cadastrou')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.tipoquestionario', verbose_name='Nome do Questionario')),
            ],
            options={
                'verbose_name': 'Resposta de Questionário',
                'verbose_name_plural': 'Respostas de Questionários',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RespostasAlternativoQuestionario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('valor', models.TextField(max_length=2800, verbose_name='Resposta')),
                ('dataCadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
                ('dataAlteracao', models.DateTimeField(auto_now=True, verbose_name='Última Alteração')),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.itemquestionario', verbose_name='Pergunta do Questionario')),
                ('quemRespondeu', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='siteCecane.quemrespondeu', verbose_name='Quem Respondeu')),
                ('questionario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.tipoquestionario', verbose_name='Nome do Questionario')),
            ],
            options={
                'verbose_name': 'Resposta Alternativo',
                'verbose_name_plural': 'Respostas Alternativas',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='itemquestionario',
            name='questionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='siteCecane.tipoquestionario', verbose_name='Nome do Questionario'),
        ),
    ]
