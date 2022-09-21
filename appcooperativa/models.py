from django.db import models
#from xml.dom.minidom import Document

class Cliente(models.Model):
    documento=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    correo=models.CharField(max_length=20)
    celular=models.CharField(max_length=15)

    # def __str__(self) -> str:
    #    return self.documento, self.nombre, self.apellido, self.celular, self.correo, self.celular

class Lineas_De_Credito(models.Model):
    codigo=models.IntegerField(primary_key=True)
    nombre=models.CharField(max_length=30)
    plazomax=models.IntegerField()
    montomaximo=models.IntegerField()

class Credito(models.Model):
    codigo_credito=models.IntegerField(primary_key=True)
    montoprestado=models.IntegerField()
    fecha=models.DateField()
    documento=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    codigo=models.ForeignKey(Lineas_De_Credito, on_delete=models.CASCADE)

class Usuario(models.Model):
    Document = models.IntegerField(primary_key=True)
    nameuser = models.CharField(max_length=30)
    password = models.CharField(max_length=60)
    rol = models.CharField(max_length=30)
    documento = models.ForeignKey(Cliente, on_delete=models.CASCADE)