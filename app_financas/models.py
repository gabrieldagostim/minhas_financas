from django.db import models

# Create your models here.

# Aqui criamos as coisas que vamos colocar no banco de dados, as informações que
# vamos armazenar no banco de dados
# classes ->  e criamos tabelas atraves das classes

class Usuario(models.Model):
    nome = models.CharField(max_length=50)


class Categoria(models.Model):
    data_criado_em = models.DateField(auto_now=True)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nome}'

class Transacao(models.Model):
    """
    Representa uma transação financeira no sistema.
    Atributos:
        data_criado_em (DateTimeField): Data e hora em que a transação foi criada. Atualizado automaticamente.
        descricao (CharField): Descrição da transação, com um limite de 50 caracteres.
        valor (FloatField): Valor monetário da transação.
        categoria (ForeignKey): Categoria associada à transação. Pode ser nula e utiliza SET_NULL ao ser excluída.
    Métodos:
        __str__(): Retorna uma representação em string da transação no formato 'dd/mm/aaaa - descricao'.
    """
    data_criado_em = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=50)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.data_criado_em.strftime("%d/%m/%Y")} - {self.descricao}'
    