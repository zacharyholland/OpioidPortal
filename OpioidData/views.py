from django.shortcuts import render
from .models import Prescriber, Drug
from django.db.models import Q
from .forms import SearchDrugsForm

# Create your views here.
def indexPageView(request) :
    return render(request, 'OpioidData/index.html')

def allPrescriberPageView(request) :
    data = Prescriber.objects.all()

    context = {
        "prescriber" : data
    }

    return render(request, 'OpioidData/prescribers.html', context)

def allDrugsPageView(request) :
    data = Drug.objects.all()

    context = {
        "drug" : data
    }

    return render(request, 'OpioidData/drugs.html', context)

def singlePrescriberPageView(request) :
    return render(request, 'OpioidData/prescriber.html')

def trendsPageView(request) :
    return render(request, 'OpioidData/trends.html')

def editPageView(request, npi) :
    data = Prescriber.objects.get(npi = npi)

    context = {
        "record" : data
    }

    return render(request, 'OpioidData/edit.html', context)

def singleDrugPageView(request) :
    return render(request, 'OpioidData/drug.html')

def updatePageView(request) :
    if request.method == 'POST' :
        npi = request.POST['npi']

        prescriber = Prescriber.objects.get(npi=npi)

        prescriber.Fname = request.POST['Fname']
        prescriber.Lname = request.POST['Lname']
        prescriber.Gender = request.POST['Gender']
        prescriber.State = request.POST['State']

        prescriber.save()

    return allPrescriberPageView(request)

def deletePageView(request, npi) :
    data = Prescriber.objects.get(npi=npi)

    data.delete()

    return allPrescriberPageView(request)

def addPageView(request) :
    if request.method == 'POST' :
        prescriber = Prescriber()

        prescriber.npi = request.POST['npi']
        prescriber.Fname = request.POST['Fname']
        prescriber.Lname = request.POST['Lname']
        prescriber.Gender = request.POST['Gender']
        prescriber.State = request.POST['State']

        prescriber.save()

        return allPrescriberPageView(request)
    else :
        return render(request, "OpioidData/add.html")

def searchDrugsPageView(request, search) :

    context = {
        "drug" : Drug.objects.filter(drugname__icontains=search)
    }

    return render(request, "OpioidData/drugsearch.html", context)