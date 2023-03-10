# Generated by Django 4.1.2 on 2022-10-30 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_index=True, max_length=70, unique=True)),
                ('slug', models.SlugField(max_length=70)),
                ('observacao', models.CharField(blank=True, max_length=70)),
            ],
            options={
                'db_table': 'genero',
                'ordering': ['-nome'],
            },
        ),
    ]
