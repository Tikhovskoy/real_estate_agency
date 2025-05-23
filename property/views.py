from django.shortcuts import render
from property.models import Flat
from django.utils.text import slugify


def format_price(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def show_flats(request):
    town = request.GET.get('town')
    min_price = format_price(request.GET.get('min_price'))
    max_price = format_price(request.GET.get('max_price'))
    new_building = request.GET.get('new_building')

    active_town = slugify(town) if town else None

    flats = Flat.objects.all()
    if town:
        flats = flats.filter(town=town)
    if min_price:
        flats = flats.filter(price__gte=min_price)
    if max_price:
        flats = flats.filter(price__lte=max_price)
    if new_building == '1':
        flats = flats.filter(new_building=True)

    towns = sorted(set(Flat.objects.values_list('town', flat=True)))
    towns_with_slugs = [(town, slugify(town)) for town in towns]
    
    return render(request, 'flats_list.html', {
        'flats': flats[:10],
        'towns': towns_with_slugs,
        'active_town': active_town,
        'max_price': max_price,
        'min_price': min_price,
        'new_building': new_building 
    })
