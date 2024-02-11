from django.shortcuts import render

from manager.models import Clubs

# from .models import Photos
# def intro1(request):
#     photos = Photos.objects.filter()
#
#     context = {'photo': photos[len(photos-1)]}
#
#     return render(request, 'intro/intro1.html', context)

def intro1(request):
    clubs = Clubs.objects.filter()
    context = {'clubs' : clubs[len(clubs)-1]}
    return render(request, 'intro/intro1.html', context)

def intro2(request):
    clubs = Clubs.objects.filter()
    context = {'clubs' : clubs[len(clubs)-1]}
    return render(request, 'intro/intro2.html', context)

def intro3(request):
    clubs = Clubs.objects.filter()
    context = {'clubs' : clubs[len(clubs)-1]}
    return render(request, 'intro/intro3.html', context)

def intro4(request):
    clubs = Clubs.objects.filter()
    context = {'clubs': clubs[len(clubs) - 1]}
    return render(request, 'intro/intro4.html', context)

def intro5(request):
    clubs = Clubs.objects.filter()
    context = {'clubs': clubs[len(clubs) - 1]}
    return render(request, 'intro/intro5.html', context)