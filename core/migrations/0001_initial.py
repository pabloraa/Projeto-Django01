# Generated by Django 5.0.6 on 2024-07-01 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250, verbose_name='Nome')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Preço')),
                ('estoque', models.IntegerField(verbose_name='Quantidade em Estoque')),
            ],
        ),
    ]
