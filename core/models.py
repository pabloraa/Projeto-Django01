from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length = 250);
    preco = models.DecimalField('Preço', decimal_places = 2, max_digits = 9)
    estoque = models.IntegerField('Quantidade em Estoque')

    def __str__(self): #apresenta o objeto instanciado de acordo com o que a gente quer
        return f'{self.nome} {self.estoque} {self.preco}'

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length = 100);
    sobrenome = models.CharField('Sobrenome' , max_length = 100)
    email = models.EmailField('Email', max_length = 100)
    def __str__(self): # apresenta o objeto instanciado de acordo com o que a gente quer
        return f'{self.nome}'