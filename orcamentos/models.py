from django.db import models
from django_cpf_cnpj.fields import CPFField, CNPJField


# Create your models here.
class CadastroClientes(models.Model):
    name = models.CharField(verbose_name='Nome' ,max_length=120, blank=True, null=True)
    dt_create = models.DateTimeField(auto_now_add=True, editable=False)
    cnpj = CNPJField(verbose_name='CNPJ',masked=False)
    email = models.EmailField(verbose_name='E-mail', max_length=254, blank=True, null=True)
    lon = models.CharField(verbose_name='Longitude',max_length=100)
    lat = models.CharField(verbose_name='Latitude',max_length=100)

    def __str__(self) -> str:
        return self.name

    # def __unicode__(self):
        # return 

class CadastroServico(models.Model):
    name = models.CharField(verbose_name='Nome do Serviço',max_length=120,blank=True, null=True)
    service_create = models.DateTimeField(auto_now_add=True, editable=False)
    descricao = models.TextField(verbose_name='Descrição')

    def __str__(self):
        return self.name


class Proposta(models.Model):
    name = models.CharField(verbose_name='Nome',max_length=120,blank=True, null=True)
    solicitante = models.ForeignKey('CadastroClientes', on_delete=models.CASCADE)
    servico = models.ManyToManyField('CadastroServico',)
    dt_servico = models.DateField(verbose_name='Data do Serviço', null=True, blank=True)
    desc_prop = models.TextField(verbose_name='Descrição', null=True, blank=True)
    valor = models.FloatField()

    def __str__(self)-> str:
        return self.name
