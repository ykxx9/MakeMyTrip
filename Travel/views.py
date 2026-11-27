
from django.shortcuts import render

def home(request):
    return render(request, 'travel/home.html')


def service_page(request, page_title):
    return render(request, 'travel/service.html', {
        'page_title': page_title
    })


def offers(request):
    return service_page(request, 'Exclusive Offers')


def flight_results(request):
    context = {
        'trip_type': request.GET.get('trip_type', 'one_way'),
        'from_city': request.GET.get('from', ''),
        'to_city': request.GET.get('to', ''),
        'departure': request.GET.get('departure', ''),
        'return_date': request.GET.get(
            'return_date',
            request.GET.get('return', '')
        ),
        'travellers': request.GET.get('travellers', '1'),
    }

    return render(request, 'travel/flights.html', context)


def flight_search(request):
    return render(request, 'travel/flight_search.html')
