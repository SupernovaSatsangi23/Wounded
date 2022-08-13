from django.shortcuts import render
from . models import HumanDiseaseArchive, HumanInjuryArchive, HumanPsychologyArchive, AnimalDiseaseArchive, AnimalInjuryArchive, FactsArchive, ProductLinks, HomePageViews, OnlineSaleViews
import datetime

import stripe
from django.conf import settings

# Create your views here.
def home(request):
	HomePageViews_object = HomePageViews.objects.get(id=1)
	HomePageViews_object.view_count = HomePageViews_object.view_count + 1
	HomePageViews_object.save()

	context = {'year' : str(datetime.datetime.now().year), 'hpv': HomePageViews.objects.only('view_count')}
	return render(request, 'healtharchive/home.html', context)


def human(request):
	context = {}
	return render(request, 'healtharchive/human.html', context)


def animal(request):
	context = {}
	return render(request, 'healtharchive/animal.html', context)


def human_disease_archive(request):
	context = {'humandiseasearchive': HumanDiseaseArchive.objects.all()}
	return render(request, 'healtharchive/human_disease_archive.html', context)


def human_injury_archive(request):
	context = {'humaninjuryarchive': HumanInjuryArchive.objects.all()}
	return render(request, 'healtharchive/human_injury_archive.html', context)


def human_psychology_archive(request):
	context = {'humanpsychologyarchive': HumanPsychologyArchive.objects.all()}
	return render(request, 'healtharchive/human_psychology_archive.html', context)


def animal_disease_archive(request):
	context = {'animaldiseasearchive': AnimalDiseaseArchive.objects.all()}
	return render(request, 'healtharchive/animal_disease_archive.html', context)


def animal_injury_archive(request):
	context = {'animalinjuryarchive': AnimalInjuryArchive.objects.all()}
	return render(request, 'healtharchive/animal_injury_archive.html', context)


def facts_archive(request):
	context = {'factsarchive': FactsArchive.objects.all()}
	return render(request, 'healtharchive/facts_archive.html', context)


def products(request):
	productLinks_object = ProductLinks.objects.get(id=1)
	productLinks_object.view_count = productLinks_object.view_count + 1
	productLinks_object.save()

	context = {'vc': ProductLinks.objects.only('view_count')}
	return render(request, 'healtharchive/products.html', context)


def onlinesale(request):
	onlinesale_object = OnlineSaleViews.objects.get(id=1)
	onlinesale_object.view_count = onlinesale_object.view_count + 1
	onlinesale_object.save()

	context = {'osv': OnlineSaleViews.objects.only('view_count')}
	return render(request, 'healtharchive/onlinesale.html', context)


stripe.api_key = settings.STRIPE_SECRET_KEY
def checkout(request):
	publishKey = settings.STRIPE_PUBLISHABLE_KEY

	if request.method == 'POST':
		token = request.POST['stripeToken']
		# print(token)
		try:# Verify your integration in this guide by including this parameter
			charge = stripe.Charge.create(amount=7099, currency='inr', source=token, description="Charged by +WOUNDED",)
		except stripe.error.CardError as e:
			pass
	context = {'publishKey' : publishKey}
	return render(request, 'healtharchive/checkout.html', context)