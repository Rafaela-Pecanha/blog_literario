# Generated by Django 4.1.4 on 2022-12-14 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livros', '0002_alter_livros_imagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='livros',
            name='autor',
            field=models.CharField(default=231, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='cep',
            field=models.CharField(default=123, max_length=70),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='isbn',
            field=models.CharField(default=123, max_length=70, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='livros',
            name='rua',
            field=models.CharField(default=123, max_length=70),
            preserve_default=False,
        ),
    ]
