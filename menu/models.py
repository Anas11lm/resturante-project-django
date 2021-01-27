from django.db import models

# Create your models here.
class Specialty(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True,blank=True,)
	ingredients = models.CharField(max_length=500)
	def __str__(self):
		return self.name


class Start(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(upload_to='photos/straters/%Y/%m/%d/')
	ingredients = models.CharField(max_length=500)
	def __str__(self):
		return self.name

class Salad(models.Model):
	name = models.CharField(max_length=200)
	price = models.FloatField()
	image = models.ImageField(upload_to='photos/salad/%Y/%m/%d/')
	ingredients = models.CharField(max_length=500)
	def __str__(self):
		return self.name



