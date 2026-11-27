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


def check_hotel_price_match(price, selected_ranges):
    """Checks if hotel price falls within any selected price range."""
    if not selected_ranges:
        return True
    for r in selected_ranges:
        if r == 'budget' and price < 2500:
            return True
        if r == 'mid' and 2500 <= price <= 6000:
            return True
        if r == 'premium' and 6000 < price <= 10000:
            return True
        if r == 'luxury' and price > 10000:
            return True
    return False


def filter_and_sort_hotels(hotels, selected_prices=None, selected_stars=None,
                           selected_ratings=None, selected_amenities=None,
                           sort_by='recommended'):
    """
    Filters and sorts hotel listings in pure Python, replacing client-side JavaScript.
    """
    filtered = []
    for h in hotels:
        # 1. Price range filter
        if selected_prices and not check_hotel_price_match(h['price'], selected_prices):
            continue

        # 2. Star rating filter
        if selected_stars and str(h['stars']) not in selected_stars:
            continue

        # 3. User review score filter
        if selected_ratings:
            match_rating = False
            for min_r in selected_ratings:
                try:
                    if h['rating'] >= float(min_r):
                        match_rating = True
                        break
                except ValueError:
                    pass
            if not match_rating:
                continue

        # 4. Amenities filter
        if selected_amenities:
            hotel_amenities_lower = [a.lower() for a in h.get('amenities', [])]
            match_all_amenities = True
            for a in selected_amenities:
                if a == 'cancellation':
                    if not h.get('free_cancellation', False):
                        match_all_amenities = False
                        break
                else:
                    if not any(a.lower() in item for item in hotel_amenities_lower):
                        match_all_amenities = False
                        break
            if not match_all_amenities:
                continue

        filtered.append(h)

    # Sorting
    if sort_by == 'price_low':
        filtered.sort(key=lambda x: x['price'])
    elif sort_by == 'price_high':
        filtered.sort(key=lambda x: x['price'], reverse=True)
    elif sort_by == 'rating_high':
        filtered.sort(key=lambda x: x['rating'], reverse=True)
    else:
        filtered.sort(key=lambda x: x['id'])

    return filtered


def get_sample_flights(from_city=None, to_city=None):
    """
    Returns realistic domestic flight options between two cities.
    """
    origin = from_city or 'New Delhi'
    destination = to_city or 'Mumbai'
    return [
        {
            'id': 1,
            'airline': 'IndiGo',
            'airline_slug': 'indigo',
            'flight_code': '6E - Sample Flight',
            'from_city': origin,
            'to_city': destination,
            'departure_time': '06:00',
            'arrival_time': '08:15',
            'duration': '2h 15m',
            'duration_minutes': 135,
            'stops': 0,
            'stops_label': 'Non Stop',
            'price': 4500,
            'price_formatted': '4,500',
            'recommended_rank': 1,
        },
        {
            'id': 2,
            'airline': 'Air India',
            'airline_slug': 'air-india',
            'flight_code': 'AI - Sample Flight',
            'from_city': origin,
            'to_city': destination,
            'departure_time': '09:30',
            'arrival_time': '12:00',
            'duration': '2h 30m',
            'duration_minutes': 150,
            'stops': 0,
            'stops_label': 'Non Stop',
            'price': 5200,
            'price_formatted': '5,200',
            'recommended_rank': 2,
        },
        {
            'id': 3,
            'airline': 'Akasa Air',
            'airline_slug': 'akasa-air',
            'flight_code': 'QP - Sample Flight',
            'from_city': origin,
            'to_city': destination,
            'departure_time': '14:00',
            'arrival_time': '16:20',
            'duration': '2h 20m',
            'duration_minutes': 140,
            'stops': 0,
            'stops_label': 'Non Stop',
            'price': 4850,
            'price_formatted': '4,850',
            'recommended_rank': 3,
        },
        {
            'id': 4,
            'airline': 'SpiceJet',
            'airline_slug': 'spicejet',
            'flight_code': 'SG - Sample Flight',
            'from_city': origin,
            'to_city': destination,
            'departure_time': '18:45',
            'arrival_time': '22:15',
            'duration': '3h 30m',
            'duration_minutes': 210,
            'stops': 1,
            'stops_label': '1 Stop',
            'price': 3999,
            'price_formatted': '3,999',
            'recommended_rank': 4,
        },
    ]


def get_flight_time_category(time_string):
    """
    Categorizes departure time ('06:00') into early, morning, afternoon, or evening.
    """
    try:
        hour = int(time_string.split(':')[0])
    except (ValueError, IndexError):
        hour = 0
    if hour < 6:
        return 'early'
    elif hour < 12:
        return 'morning'
    elif hour < 18:
        return 'afternoon'
    else:
        return 'evening'


def filter_and_sort_flights(flights, stops=None, times=None, airlines=None, sort_by='recommended'):
    """
    Filters and sorts a list of flights using pure Python logic, replacing JavaScript.
    """
    filtered = []
    for fl in flights:
        # 1. Stops filter
        if stops:
            match_stop = False
            for s in stops:
                if s == '2' and fl['stops'] >= 2:
                    match_stop = True
                    break
                elif str(fl['stops']) == s:
                    match_stop = True
                    break
            if not match_stop:
                continue

        # 2. Time category filter
        if times:
            cat = get_flight_time_category(fl['departure_time'])
            if cat not in times:
                continue

        # 3. Airline filter
        if airlines:
            if fl['airline_slug'] not in airlines:
                continue

        filtered.append(fl)

    # Sorting
    if sort_by == 'cheapest':
        filtered.sort(key=lambda x: x['price'])
    elif sort_by == 'fastest':
        filtered.sort(key=lambda x: x['duration_minutes'])
    else:
        filtered.sort(key=lambda x: x['recommended_rank'])

    return filtered


def get_sample_holiday_packages(destination_filter=None, theme_filter=None):
    """
    Returns curated holiday tour packages with inclusions, ratings, and pricing.
    Supports filtering by destination keyword or theme.
    """
    packages = [
        {
            'id': 1,
            'title': 'Magical Kashmir Valley with Luxury Houseboat Stay',
            'destination': 'Kashmir',
            'duration': '5 Days / 4 Nights',
            'price': '18,499',
            'original_price': '24,000',
            'rating': 4.9,
            'reviews_count': '1,240',
            'theme': 'Honeymoon',
            'inclusions': ['Flights Included', '4-Star Hotels', 'Daily Breakfast & Dinner', 'Dal Lake Shikara', 'Private Cab'],
            'image': 'travel/images/kashmir.jpg',
            'is_static_image': True,
        },
        {
            'id': 2,
            'title': 'Goa Beachfront Escape with Sunset Island Cruise',
            'destination': 'Goa',
            'duration': '4 Days / 3 Nights',
            'price': '12,999',
            'original_price': '17,500',
            'rating': 4.8,
            'reviews_count': '2,150',
            'theme': 'Beach',
            'inclusions': ['Beachfront Resort', 'Airport Transfers', 'North & South Goa Tours', 'Water Sports Pass', 'Breakfast'],
            'image': 'travel/images/goa.jpg',
            'is_static_image': True,
        },
        {
            'id': 3,
            'title': 'Scenic Kerala Backwaters & Munnar Tea Plantation',
            'destination': 'Kerala',
            'duration': '6 Days / 5 Nights',
            'price': '21,500',
            'original_price': '28,000',
            'rating': 4.9,
            'reviews_count': '980',
            'theme': 'Family',
            'inclusions': ['Deluxe Houseboat Stay', 'Munnar Hill Resort', 'Spice Plantation Tour', 'Private AC Cab', 'All Meals'],
            'image': 'travel/images/kerala.jpg',
            'is_static_image': True,
        },
        {
            'id': 4,
            'title': 'Himachal Snow Adventure & Rohtang Pass Excursion',
            'destination': 'Manali',
            'duration': '5 Days / 4 Nights',
            'price': '15,800',
            'original_price': '21,000',
            'rating': 4.7,
            'reviews_count': '1,410',
            'theme': 'Mountains',
            'inclusions': ['Mountain View Resort', 'Solang Valley Tour', 'Rohtang Pass Permit', 'Bonfire Night', 'Daily Meals'],
            'image': 'travel/images/manali.jpg',
            'is_static_image': True,
        },
        {
            'id': 5,
            'title': 'Royal Rajasthan Heritage, Forts & Desert Safari',
            'destination': 'Rajasthan',
            'duration': '6 Days / 5 Nights',
            'price': '24,999',
            'original_price': '32,000',
            'rating': 4.8,
            'reviews_count': '870',
            'theme': 'Heritage',
            'inclusions': ['Heritage Haveli Stays', 'Sam Sand Dunes Camp', 'Camel Safari & Folk Dance', 'Fort Entry Passes'],
            'image': 'https://images.unsplash.com/photo-1599661046289-e31897846e41?w=600&auto=format&fit=crop&q=80',
            'is_static_image': False,
        },
        {
            'id': 6,
            'title': 'Andaman Island Paradise with Coral Reef Scuba Diving',
            'destination': 'Andaman',
            'duration': '6 Days / 5 Nights',
            'price': '28,999',
            'original_price': '36,500',
            'rating': 4.9,
            'reviews_count': '1,110',
            'theme': 'Adventure',
            'inclusions': ['Radhanagar Beach Resort', 'Havelock Island Cruise Ferry', 'Intro Scuba Session', 'Cellular Jail Light & Sound'],
            'image': 'https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?w=600&auto=format&fit=crop&q=80',
            'is_static_image': False,
        },
    ]

    # Filter by destination keyword if provided
    if destination_filter and destination_filter.strip():
        search_query = destination_filter.strip().lower()
        packages = [
            pkg for pkg in packages
            if search_query in pkg['destination'].lower() or search_query in pkg['title'].lower()
        ]

    # Filter by theme category if provided
    if theme_filter and theme_filter.strip() and theme_filter.strip().lower() != 'all':
        theme_query = theme_filter.strip().lower()
        packages = [
            pkg for pkg in packages
            if theme_query == pkg['theme'].lower()
        ]

    return packages


def get_sample_trains(from_station=None, to_station=None):
    """
    Returns realistic train listings for Indian Railways with running days,
    stations, timings, duration, and seat availability across classes.
    """
    origin = from_station or 'New Delhi (NDLS)'
    destination = to_station or 'Varanasi Jn (BSB)'

    trains = [
        {
            'number': '22436',
            'name': 'Vande Bharat Express',
            'from_station': origin,
            'to_station': destination,
            'departure_time': '06:00',
            'arrival_time': '14:00',
            'duration': '08h 00m',
            'running_days': [
                {'code': 'M', 'name': 'Mon', 'active': True},
                {'code': 'T', 'name': 'Tue', 'active': True},
                {'code': 'W', 'name': 'Wed', 'active': True},
                {'code': 'T', 'name': 'Thu', 'active': False},
                {'code': 'F', 'name': 'Fri', 'active': True},
                {'code': 'S', 'name': 'Sat', 'active': True},
                {'code': 'S', 'name': 'Sun', 'active': True},
            ],
            'classes': [
                {'code': 'CC', 'name': 'AC Chair Car', 'price': '₹1,750', 'status': 'AVAILABLE 42', 'status_type': 'available'},
                {'code': 'EC', 'name': 'Exec Chair Car', 'price': '₹3,300', 'status': 'AVAILABLE 12', 'status_type': 'available'},
            ],
        },
        {
            'number': '12560',
            'name': 'Shiv Ganga Superfast Express',
            'from_station': origin,
            'to_station': destination,
            'departure_time': '20:05',
            'arrival_time': '06:10',
            'duration': '10h 05m',
            'running_days': [
                {'code': 'M', 'name': 'Mon', 'active': True},
                {'code': 'T', 'name': 'Tue', 'active': True},
                {'code': 'W', 'name': 'Wed', 'active': True},
                {'code': 'T', 'name': 'Thu', 'active': True},
                {'code': 'F', 'name': 'Fri', 'active': True},
                {'code': 'S', 'name': 'Sat', 'active': True},
                {'code': 'S', 'name': 'Sun', 'active': True},
            ],
            'classes': [
                {'code': 'SL', 'name': 'Sleeper', 'price': '₹445', 'status': 'RAC 18', 'status_type': 'rac'},
                {'code': '3A', 'name': 'AC 3 Tier', 'price': '₹1,180', 'status': 'AVAILABLE 28', 'status_type': 'available'},
                {'code': '2A', 'name': 'AC 2 Tier', 'price': '₹1,690', 'status': 'AVAILABLE 14', 'status_type': 'available'},
                {'code': '1A', 'name': 'AC 1st Class', 'price': '₹2,850', 'status': 'AVAILABLE 04', 'status_type': 'available'},
            ],
        },
        {
            'number': '15128',
            'name': 'Kashi Vishwanath Express',
            'from_station': origin,
            'to_station': destination,
            'departure_time': '11:35',
            'arrival_time': '04:40',
            'duration': '17h 05m',
            'running_days': [
                {'code': 'M', 'name': 'Mon', 'active': True},
                {'code': 'T', 'name': 'Tue', 'active': True},
                {'code': 'W', 'name': 'Wed', 'active': True},
                {'code': 'T', 'name': 'Thu', 'active': True},
                {'code': 'F', 'name': 'Fri', 'active': True},
                {'code': 'S', 'name': 'Sat', 'active': True},
                {'code': 'S', 'name': 'Sun', 'active': True},
            ],
            'classes': [
                {'code': 'SL', 'name': 'Sleeper', 'price': '₹420', 'status': 'WL 12', 'status_type': 'wl'},
                {'code': '3A', 'name': 'AC 3 Tier', 'price': '₹1,140', 'status': 'AVAILABLE 08', 'status_type': 'available'},
                {'code': '2A', 'name': 'AC 2 Tier', 'price': '₹1,630', 'status': 'AVAILABLE 06', 'status_type': 'available'},
            ],
        },
        {
            'number': '12952',
            'name': 'Mumbai Tejas Rajdhani Express',
            'from_station': origin,
            'to_station': destination,
            'departure_time': '16:55',
            'arrival_time': '08:35',
            'duration': '15h 40m',
            'running_days': [
                {'code': 'M', 'name': 'Mon', 'active': True},
                {'code': 'T', 'name': 'Tue', 'active': True},
                {'code': 'W', 'name': 'Wed', 'active': True},
                {'code': 'T', 'name': 'Thu', 'active': True},
                {'code': 'F', 'name': 'Fri', 'active': True},
                {'code': 'S', 'name': 'Sat', 'active': True},
                {'code': 'S', 'name': 'Sun', 'active': True},
            ],
            'classes': [
                {'code': '3A', 'name': 'AC 3 Tier', 'price': '₹2,420', 'status': 'AVAILABLE 64', 'status_type': 'available'},
                {'code': '2A', 'name': 'AC 2 Tier', 'price': '₹3,410', 'status': 'AVAILABLE 22', 'status_type': 'available'},
                {'code': '1A', 'name': 'AC 1st Class', 'price': '₹5,120', 'status': 'AVAILABLE 08', 'status_type': 'available'},
            ],
        },
    ]
    return trains


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
    """Clean, minimal Coming Soon page for upcoming services handled with Python."""
    service = get_coming_soon_details(service_key)
    notified = False
    email = ''

    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            notified = True
    elif request.GET.get('notified'):
        email = request.GET.get('email', '').strip()
        notified = True

    return render(request, 'travel/coming_soon.html', {
        'service': service,
        'notified': notified,
        'email': email,
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
    and filters/sorts the hotel list using pure Python logic.
    """
    today, tomorrow = get_today_and_tomorrow()

    # 1. Read search inputs from request.GET (with sensible fallbacks)
    city = request.GET.get('city', 'Goa').strip() or 'Goa'
    checkin = request.GET.get('checkin', today)
    checkout = request.GET.get('checkout', tomorrow)
    rooms = request.GET.get('rooms', '1')
    guests = request.GET.get('guests', '2')

    # 2. Read filter selections (supports multi-select)
    selected_prices = request.GET.getlist('price_category')
    selected_stars = request.GET.getlist('stars')
    selected_ratings = request.GET.getlist('rating')
    selected_amenities = request.GET.getlist('amenity')
    sort_by = request.GET.get('sort', 'recommended')

    # 3. Get hotel listings for the requested city and filter/sort in Python
    all_hotels = get_sample_hotels(city)
    filtered_hotels = filter_and_sort_hotels(
        hotels=all_hotels,
        selected_prices=selected_prices,
        selected_stars=selected_stars,
        selected_ratings=selected_ratings,
        selected_amenities=selected_amenities,
        sort_by=sort_by,
    )

    # 4. Build context dictionary for the template
    context = {
        'city': city,
        'checkin': checkin,
        'checkout': checkout,
        'rooms': rooms,
        'guests': guests,
        'hotels': filtered_hotels,
        'hotel_count': len(filtered_hotels),
        'selected_prices': selected_prices,
        'selected_stars': selected_stars,
        'selected_ratings': selected_ratings,
        'selected_amenities': selected_amenities,
        'sort_by': sort_by,
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
    validates one-way vs round-trip logic, and filters/sorts flights using pure Python.
    """
    trip_type = request.GET.get('trip_type', 'one_way')
    from_city = request.GET.get('from', 'New Delhi').strip() or 'New Delhi'
    to_city = request.GET.get('to', 'Mumbai').strip() or 'Mumbai'
    departure = request.GET.get('departure', '')
    return_date = request.GET.get('return_date', request.GET.get('return', ''))
    travellers = request.GET.get('travellers', '1')

    # Business rule: if one-way is chosen, clear the return date
    if trip_type == 'one_way':
        return_date = ''

    # Read filter query parameters (multiple values supported)
    selected_stops = request.GET.getlist('stops')
    selected_times = request.GET.getlist('time')
    selected_airlines = request.GET.getlist('airline')
    sort_by = request.GET.get('sort', 'recommended')

    all_flights = get_sample_flights(from_city=from_city, to_city=to_city)
    filtered_flights = filter_and_sort_flights(
        flights=all_flights,
        stops=selected_stops,
        times=selected_times,
        airlines=selected_airlines,
        sort_by=sort_by,
    )

    context = {
        'trip_type': trip_type,
        'from_city': from_city,
        'to_city': to_city,
        'departure': departure,
        'return_date': return_date,
        'travellers': travellers,
        'flights': filtered_flights,
        'flight_count': len(filtered_flights),
        'selected_stops': selected_stops,
        'selected_times': selected_times,
        'selected_airlines': selected_airlines,
        'sort_by': sort_by,
    }
    return render(request, 'travel/flights.html', context)


# ==============================================================================
# HOLIDAY PACKAGES & TRAINS VIEWS
# ==============================================================================

def holidays(request):
    """
    Holiday packages discovery and search view.
    Supports filtering packages by destination, theme, and duration.
    """
    today, tomorrow = get_today_and_tomorrow()
    destination = request.GET.get('destination', '').strip()
    theme = request.GET.get('theme', '').strip()
    from_city = request.GET.get('from_city', 'New Delhi').strip()
    duration = request.GET.get('duration', '').strip()
    travel_date = request.GET.get('date', today)

    packages = get_sample_holiday_packages(
        destination_filter=destination,
        theme_filter=theme,
    )

    context = {
        'today': today,
        'tomorrow': tomorrow,
        'travel_date': travel_date,
        'from_city': from_city,
        'destination': destination,
        'current_theme': theme,
        'duration': duration,
        'packages': packages,
    }
    return render(request, 'travel/holidays.html', context)


def trains(request):
    """
    Train ticket search and IRCTC booking view with pure Python logic.
    Handles mode switching (book, pnr, live) and PNR/live train lookups.
    """
    today, tomorrow = get_today_and_tomorrow()
    mode = request.GET.get('mode', 'book')
    from_station = request.GET.get('from_station', 'New Delhi (NDLS)').strip()
    to_station = request.GET.get('to_station', 'Varanasi Jn (BSB)').strip()
    travel_date = request.GET.get('date', today)
    train_class = request.GET.get('train_class', '').strip()
    quota = request.GET.get('quota', 'GN').strip()

    # PNR Status Check in Python
    pnr_query = request.GET.get('pnr', '').strip()
    pnr_result = None
    pnr_error = None
    if pnr_query:
        mode = 'pnr'
        if len(pnr_query) == 10 and pnr_query.isdigit():
            pnr_result = {
                'pnr': pnr_query,
                'status': 'CONFIRMED (CNF)',
                'train': '22436 Vande Bharat Exp',
                'coach': 'C4',
                'berth': '24 (Window)',
            }
        else:
            pnr_error = 'Please enter a valid 10-digit IRCTC PNR number.'

    # Live Train Status Check in Python
    train_num_query = request.GET.get('train_number', '').strip()
    live_result = None
    live_error = None
    if train_num_query:
        mode = 'live'
        live_result = {
            'number': train_num_query,
            'status': 'Running On Time',
            'last_departed': 'Kanpur Central (CNB) at 10:12 AM',
            'next_halt': 'Prayagraj Jn (PRYJ) · Expected at 12:08 PM (Platform 6)',
        }

    train_list = get_sample_trains(
        from_station=from_station,
        to_station=to_station,
    )

    context = {
        'today': today,
        'tomorrow': tomorrow,
        'travel_date': travel_date,
        'from_station': from_station,
        'to_station': to_station,
        'train_class': train_class,
        'quota': quota,
        'trains': train_list,
        'mode': mode,
        'pnr_query': pnr_query,
        'pnr_result': pnr_result,
        'pnr_error': pnr_error,
        'train_num_query': train_num_query,
        'live_result': live_result,
        'live_error': live_error,
    }
    return render(request, 'travel/trains.html', context)
