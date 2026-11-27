from datetime import date, timedelta
from django.shortcuts import render


# ==============================================================================
# HELPER FUNCTIONS (Reusable functions to keep views simple and clean)
# ==============================================================================

def get_today_and_tomorrow():
    """
    Returns today's and tomorrow's date formatted as 'YYYY-MM-DD'.
    This is widely used across booking forms for minimum dates.
    """
    today = date.today()
    tomorrow = today + timedelta(days=1)
    return today.isoformat(), tomorrow.isoformat()


def get_trending_destinations():
    """Returns sample trending destinations shown on the hotel landing page."""
    return [
        {
            'name': 'Goa',
            'tag': 'Beach & Parties',
            'properties': '4,500+ Properties',
            'image': 'travel/images/goa.jpg',
            'avg_price': '₹2,499',
        },
        {
            'name': 'Manali',
            'tag': 'Mountains & Snow',
            'properties': '2,800+ Properties',
            'image': 'travel/images/manali.jpg',
            'avg_price': '₹1,999',
        },
        {
            'name': 'Kashmir',
            'tag': 'Paradise & Valleys',
            'properties': '1,900+ Properties',
            'image': 'travel/images/kashmir.jpg',
            'avg_price': '₹3,200',
        },
        {
            'name': 'Kerala',
            'tag': 'Backwaters & Nature',
            'properties': '3,100+ Properties',
            'image': 'travel/images/kerala.jpg',
            'avg_price': '₹2,799',
        },
    ]


def get_popular_flight_routes():
    """Returns popular domestic flight sectors for quick selection."""
    return [
        {
            'from_city': 'New Delhi',
            'to_city': 'Mumbai',
            'tag': 'Business & Capital',
            'duration': '2h 15m · Non-stop',
            'price': '₹4,500',
            'image': 'travel/images/goa.jpg',
        },
        {
            'from_city': 'Mumbai',
            'to_city': 'Goa',
            'tag': 'Beach & Weekend',
            'duration': '1h 20m · Non-stop',
            'price': '₹3,200',
            'image': 'travel/images/goa.jpg',
        },
        {
            'from_city': 'New Delhi',
            'to_city': 'Srinagar',
            'tag': 'Himalayan Escape',
            'duration': '1h 35m · Non-stop',
            'price': '₹4,850',
            'image': 'travel/images/kashmir.jpg',
        },
        {
            'from_city': 'Bengaluru',
            'to_city': 'Kochi',
            'tag': 'Coast & Backwaters',
            'duration': '1h 10m · Non-stop',
            'price': '₹2,990',
            'image': 'travel/images/kerala.jpg',
        },
    ]


def get_sample_hotels(city):
    """
    Returns a sample list of hotels for a given city with different star levels,
    prices, and amenities so users can test searching, sorting, and filtering.
    """
    return [
        {
            'id': 1,
            'name': f'The Grand {city} Resort & Luxury Spa',
            'stars': 5,
            'star_label': '5 Star Luxury',
            'location': f'Prime Beachfront Area, {city}',
            'distance': '350m from center',
            'rating': 4.8,
            'rating_label': 'Excellent',
            'reviews_count': '2,840',
            'price': 11500,
            'original_price': 15000,
            'taxes': 1380,
            'image': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free Breakfast', 'Swimming Pool', 'Spa & Wellness', 'Free WiFi', 'Couple Friendly'],
            'free_cancellation': True,
            'room_type': 'Deluxe Ocean View King Suite',
        },
        {
            'id': 2,
            'name': f'Royal Heritage Palace & Suites {city}',
            'stars': 4,
            'star_label': '4 Star Premium',
            'location': f'Heritage Boulevard, {city}',
            'distance': '1.2 km from main market',
            'rating': 4.5,
            'rating_label': 'Very Good',
            'reviews_count': '1,620',
            'price': 5400,
            'original_price': 7200,
            'taxes': 650,
            'image': 'https://images.unsplash.com/photo-1582719508461-905c673771fd?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free Breakfast', 'Free WiFi', 'Swimming Pool', 'Multi-Cuisine Restaurant'],
            'free_cancellation': True,
            'room_type': 'Executive Garden View Room',
        },
        {
            'id': 3,
            'name': f'Silver Palm Waterfront Boutique Hotel',
            'stars': 4,
            'star_label': '4 Star Boutique',
            'location': f'Scenic Coastal Road, {city}',
            'distance': '600m from promenade',
            'rating': 4.6,
            'rating_label': 'Excellent',
            'reviews_count': '980',
            'price': 7800,
            'original_price': 9900,
            'taxes': 940,
            'image': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free Breakfast', 'Free Cancellation', 'Swimming Pool', 'Couple Friendly', 'Bar & Lounge'],
            'free_cancellation': True,
            'room_type': 'Premium Poolside Suite',
        },
        {
            'id': 4,
            'name': f'Cozy Nest Boutique Suites',
            'stars': 3,
            'star_label': '3 Star Comfort',
            'location': f'Central Tourist Hub, {city}',
            'distance': '450m from shopping district',
            'rating': 4.2,
            'rating_label': 'Very Good',
            'reviews_count': '750',
            'price': 3200,
            'original_price': 4500,
            'taxes': 380,
            'image': 'https://images.unsplash.com/photo-1520250497591-112f2f40a3f4?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free WiFi', 'Air Conditioning', 'Free Cancellation', 'Couple Friendly'],
            'free_cancellation': True,
            'room_type': 'Standard Deluxe Double',
        },
        {
            'id': 5,
            'name': f'Urban Stay Comfort Inn & Suites',
            'stars': 3,
            'star_label': '3 Star Business',
            'location': f'Commercial Junction, {city}',
            'distance': '2.5 km from transit station',
            'rating': 4.0,
            'rating_label': 'Good',
            'reviews_count': '1,120',
            'price': 2400,
            'original_price': 3400,
            'taxes': 290,
            'image': 'https://images.unsplash.com/photo-1590490360182-c33d57733427?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free WiFi', 'Free Breakfast', '24h Room Service', 'Air Conditioning'],
            'free_cancellation': False,
            'room_type': 'Classic Business Twin Room',
        },
        {
            'id': 6,
            'name': f'Backpackers Haven & Social Hostel',
            'stars': 2,
            'star_label': 'Budget Friendly',
            'location': f'Old Town Lane, {city}',
            'distance': '800m from historic center',
            'rating': 3.9,
            'rating_label': 'Good',
            'reviews_count': '510',
            'price': 1350,
            'original_price': 1900,
            'taxes': 160,
            'image': 'https://images.unsplash.com/photo-1555854877-bab0e564b8d5?w=600&auto=format&fit=crop&q=80',
            'amenities': ['Free WiFi', 'Air Conditioning', 'Cafe & Lounge'],
            'free_cancellation': True,
            'room_type': 'Private Bunk / Solo Pod',
        },
    ]


def get_coming_soon_details(service_key, default_title='Service'):
    """
    Returns structured data for the Coming Soon page based on the requested service.
    This provides rich preview information for Buses, Tours, Visa, Forex, and Insurance.
    """
    services_data = {
        'buses': {
            'title': 'Buses',
            'tagline': 'Intercity & Sleeper Bus Bookings',
            'description': 'We are partnering with state RTCs and top private bus operators across India to bring you reliable, comfortable, and affordable bus journeys.',
            'icon': 'travel/images/icon_buses.svg',
            'features': [
                'Live GPS bus tracking and status updates',
                'Comfortable Sleeper, AC, and Luxury Volvo buses',
                'Zero convenience fee launch discounts',
                'Instant ticket confirmation delivered on WhatsApp',
            ],
        },
        'tours': {
            'title': 'Tours & Attractions',
            'tagline': 'Curated Sightseeing, Activities & Day Trips',
            'description': 'Discover top-rated city tours, skip-the-line museum tickets, adventure sports, and scenic excursions with certified local guides.',
            'icon': 'travel/images/icon_tours.svg',
            'features': [
                'Guaranteed entry and skip-the-line passes',
                'Verified local tour operators and English-speaking guides',
                'Instant digital mobile vouchers with instant booking',
                'Flexible cancellation and 100% refund on select activities',
            ],
        },
        'visa': {
            'title': 'Visa Services',
            'tagline': 'Hassle-Free Tourist & Business Visas',
            'description': 'Simplifying the visa process for over 50 destinations worldwide with door-step document pickup, expert verification, and end-to-end tracking.',
            'icon': 'travel/images/icon_visa.svg',
            'features': [
                '99.2% visa approval assistance rate',
                'Doorstep document collection and return',
                'Dedicated visa specialist assigned to your application',
                'Real-time status updates via SMS and email',
            ],
        },
        'forex': {
            'title': 'Forex Card & Currency',
            'tagline': 'Multi-Currency Travel Cards & Foreign Cash',
            'description': 'Get zero-markup multi-currency travel cards and genuine foreign currency delivered directly to your doorstep with live interbank exchange rates.',
            'icon': 'travel/images/icon_forex.svg',
            'features': [
                'Zero foreign exchange markup on card transactions',
                'Doorstep delivery within 24 hours in major cities',
                'Lock in live exchange rates immediately with no hidden fees',
                'Accepted at over 30 million merchant stores worldwide',
            ],
        },
        'insurance': {
            'title': 'Travel Insurance',
            'tagline': 'Comprehensive Protection for Every Trip',
            'description': 'Travel with total peace of mind. Complete coverage for medical emergencies, flight cancellations, baggage loss, and trip interruptions.',
            'icon': 'travel/images/icon_insurance.svg',
            'features': [
                'Cashless hospitalization in thousands of hospitals globally',
                'Full reimbursement for flight cancellations and delays',
                'Baggage loss, theft, and delay compensation',
                '24/7 dedicated worldwide emergency assistance',
            ],
        },
        'trains': {
            'title': 'Trains',
            'tagline': 'IRCTC Authorized Train Ticket Booking',
            'description': 'Seamless Indian Railways train bookings with instant PNR status, live running tracking, and zero payment gateway charges.',
            'icon': 'travel/images/icon_trains.svg',
            'features': [
                'Official IRCTC authorized booking partner',
                'Instant PNR status and live train tracking',
                'Tatkal ticket booking support',
                'Fast refunds on ticket cancellations',
            ],
        },
        'cabs': {
            'title': 'Cabs & Taxis',
            'tagline': 'Intercity Drops, Round Trips & Airport Transfers',
            'description': 'Book clean, chauffeur-driven outstation and local taxis with transparent pricing and zero surge fees.',
            'icon': 'travel/images/icon_cabs.svg',
            'features': [
                'Clean, sanitized, and well-maintained cabs',
                'Chauffeur-driven with verified professional drivers',
                'Transparent all-inclusive rates (tolls and taxes included)',
                'Flexible pickup times with 24/7 road assistance',
            ],
        },
        'homestays': {
            'title': 'Villas & Homestays',
            'tagline': 'Handpicked Private Homes, Cottages & Farmstays',
            'description': 'Escape to private villas with swimming pools, mountain cottages, and heritage homestays curated for families and weekend getaways.',
            'icon': 'travel/images/icon_villas.svg',
            'features': [
                'Entire private homes with exclusive access',
                'Private swimming pools, gardens, and BBQ areas',
                'Caretaker on-site with authentic home-cooked meals',
                'Pet-friendly options across top holiday destinations',
            ],
        },
    }

    # Return matching service data or a sensible default
    return services_data.get(service_key, {
        'title': default_title,
        'tagline': 'We are working on bringing this service to you',
        'description': 'This feature is currently under active development and will be available soon.',
        'icon': 'travel/images/icon_hotels.svg',
        'features': [
            'Seamless booking experience',
            'Exclusive member launch discounts',
            'Instant digital confirmations',
            '24/7 customer support',
        ],
    })


# ==============================================================================
# MAIN PAGE VIEWS
# ==============================================================================

def home(request):
    """Home landing page with flight search card and featured sections."""
    today, _ = get_today_and_tomorrow()
    return render(request, 'travel/home.html', {
        'today': today,
    })


def coming_soon(request, service_key):
    """Clean, minimal Coming Soon page for upcoming services."""
    service = get_coming_soon_details(service_key)
    return render(request, 'travel/coming_soon.html', {
        'service': service,
    })


def service_page(request, page_title):
    """
    Renders coming soon view using the page title, ensuring all informational
    service pages have consistent, beautiful styling.
    """
    key = page_title.lower().replace(' & ', '_').replace(' ', '_')
    service = get_coming_soon_details(key, default_title=page_title)
    return render(request, 'travel/coming_soon.html', {
        'service': service,
    })


def offers(request):
    """Exclusive travel deals and discount offers."""
    return service_page(request, 'Exclusive Offers')


# ==============================================================================
# HOTEL VIEWS
# ==============================================================================

def hotels(request):
    """Hotels search & discovery landing page."""
    today, tomorrow = get_today_and_tomorrow()
    context = {
        'today': today,
        'tomorrow': tomorrow,
        'trending_destinations': get_trending_destinations(),
    }
    return render(request, 'travel/hotels.html', context)


def hotel_results(request):
    """
    Hotel listings view: extracts search filters from the URL query parameters
    and sends the matching hotel list to the template.
    """
    today, tomorrow = get_today_and_tomorrow()

    # 1. Read search inputs from request.GET (with sensible fallbacks)
    city = request.GET.get('city', 'Goa').strip() or 'Goa'
    checkin = request.GET.get('checkin', today)
    checkout = request.GET.get('checkout', tomorrow)
    rooms = request.GET.get('rooms', '1')
    guests = request.GET.get('guests', '2')
    price_category = request.GET.get('price_category', 'all')

    # 2. Get hotel listings for the requested city
    hotel_list = get_sample_hotels(city)

    # 3. Build context dictionary for the template
    context = {
        'city': city,
        'checkin': checkin,
        'checkout': checkout,
        'rooms': rooms,
        'guests': guests,
        'price_category': price_category,
        'hotels': hotel_list,
        'hotel_count': len(hotel_list),
        'today': today,
        'tomorrow': tomorrow,
    }
    return render(request, 'travel/hotel_results.html', context)


# ==============================================================================
# FLIGHT VIEWS
# ==============================================================================

def flight_search(request):
    """Flight search page with popular routes and minimal booking form."""
    today, tomorrow = get_today_and_tomorrow()
    context = {
        'today': today,
        'tomorrow': tomorrow,
        'popular_routes': get_popular_flight_routes(),
    }
    return render(request, 'travel/flight_search.html', context)


def flight_results(request):
    """
    Flight results view: extracts user parameters from request.GET,
    validates one-way vs round-trip logic, and renders the results page.
    """
    trip_type = request.GET.get('trip_type', 'one_way')
    from_city = request.GET.get('from', '')
    to_city = request.GET.get('to', '')
    departure = request.GET.get('departure', '')
    return_date = request.GET.get('return_date', request.GET.get('return', ''))
    travellers = request.GET.get('travellers', '1')

    # Business rule: if one-way is chosen, clear the return date
    if trip_type == 'one_way':
        return_date = ''

    context = {
        'trip_type': trip_type,
        'from_city': from_city,
        'to_city': to_city,
        'departure': departure,
        'return_date': return_date,
        'travellers': travellers,
    }
    return render(request, 'travel/flights.html', context)
