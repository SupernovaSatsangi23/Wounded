from django.db import models

# Create your models here.


class HumanDiseaseArchive(models.Model):
	name = models.TextField(null=True, blank=True)
	solution = models.TextField(null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	img = models.ImageField(upload_to ='human_disease_archive/', blank=True)

	def __str__(self):
		return self.name


class HumanInjuryArchive(models.Model):
	name = models.TextField(blank=True)
	solution = models.TextField(blank=True)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to ='human_injury_archive/', blank=True)

	def __str__(self):
		return self.name


class HumanPsychologyArchive(models.Model):
	name = models.TextField(blank=True)
	solution = models.TextField(blank=True)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to ='human_psychology_archive/', blank=True)

	def __str__(self):
		return self.name


class AnimalDiseaseArchive(models.Model):
	name = models.TextField(blank=True)
	solution = models.TextField(blank=True)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to ='animal_disease_archive/', blank=True) # null=False : means that you can use null value in database and still load pages

	def __str__(self):
		return self.name


class AnimalInjuryArchive(models.Model):
	name = models.TextField(blank=True)
	solution = models.TextField(blank=True)
	description = models.TextField(blank=True)
	img = models.ImageField(upload_to ='animal_injury_archive/', blank=True)

	def __str__(self):
		return self.name


class FactsArchive(models.Model):
	name = models.TextField(blank=True)
	description = models.TextField(blank=True)

	def __str__(self):
		return self.name


class ProductLinks(models.Model):
	view_count = models.BigIntegerField(default=0)

	def __str__(self):
		return 'view_count'


class HomePageViews(models.Model):
	view_count = models.BigIntegerField(default=0)

	def __str__(self):
		return 'view_count'


class OnlineSaleViews(models.Model):
	view_count = models.BigIntegerField(default=0)

	def __str__(self):
		return 'view_count'