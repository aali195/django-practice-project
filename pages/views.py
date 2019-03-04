from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, state_choices, bedroom_choices, price_choices

from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    # Not in use for now, homepage will not show the recent listings
    return render(request, 'pages/home.html', context)

def about(request):
    # Get all realtors
    realtors = Realtor.objects.order_by('-hire_date')
    
    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    # Also not in use for now, will not show the realtors on about page
    return render(request, 'pages/about.html', context)
