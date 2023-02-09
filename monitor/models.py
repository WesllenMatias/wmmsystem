from django.db import models

# Create your models here.
class CadastroSensore(models.Model):
    setor = models.CharField(verbose_name='Setor', max_length=50,blank=True,null=True)
    url = models.CharField(verbose_name='Url', max_length=50)
    modelo = models.CharField(verbose_name='Modelo', max_length=50)

    def __str__(self) -> str:
        return self.setor

    # def __unicode__(self):
    #     return 


