# Generated by Django 4.2.2 on 2023-06-22 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatalheTruma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aluno', models.CharField(max_length=100)),
                ('professor', models.CharField(max_length=100)),
                ('turma', models.CharField(max_length=100)),
            ],
        ),
    ]