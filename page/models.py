from django.db import models

class Expediente(models.Model):
	nro_instruccion = models.IntegerField(blank=True,null=True)
	nro_expediente = models.IntegerField(blank=True,null=True)
	anio = models.IntegerField(blank=True,null=True)
	juzgado = models.CharField(max_length=45,blank=True,null=True)
	agraviado = models.CharField(max_length=100,blank=True,null=True)
	inculpado = models.CharField(max_length=100,blank=True,null=True)
	materia = models.CharField(max_length=150,blank=True,null=True)
	nro_fojas = models.IntegerField(blank=True,null=True,verbose_name='Foja(s)')
	nro_legajo = models.IntegerField(blank=True,null=True,verbose_name='Legajo')

	def __unicode__(self):
		caso = "Expediente %s del agraviado %s e inculpado %s"%(self.nro_expediente,self.agraviado,self.inculpado)
		return caso

	class Meta:
		ordering = ['id']