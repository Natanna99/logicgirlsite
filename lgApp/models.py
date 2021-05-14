from django.db import models

class Versao(models.Model):
    nome=models.CharField("Nome da versão",max_length=50)
    versao=models.CharField("Número da versão",max_length=15)
    descricao=models.CharField("Descrição da versão",max_length=1500)
    arq=models.CharField("Local do Arquivo",max_length=1500)
    qtd_down = models.IntegerField("Quatidade de downloads",default=0)

    def __str__(self):
        return "{} - Versão: {} - quatidade de downloads: {}".format(self.nome,self.versao,self.qtd_down)

    def se_e_pa(self):
        return self.pk%2==0