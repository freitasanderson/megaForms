# Generated by Django 4.1.1 on 2023-12-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_alter_perfil_cargo_alter_perfil_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='imagem',
            field=models.ImageField(blank=True, help_text='Imagem que será mostrada em seu Perfil', null=True, upload_to='perfil', verbose_name='Imagem de Perfil'),
        ),
    ]
