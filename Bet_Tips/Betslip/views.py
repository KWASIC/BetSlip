# tips/views.py
from django.shortcuts import render, redirect
from .models import Match, BookingCode
from datetime import date, timedelta

def match_list(request):
    today_matches = Match.objects.filter(match_date=date.today())  # Only matches for today
    booking_codes = BookingCode.objects.all()  # All booking codes
    return render(request, 'match_list1.html', {'matches': today_matches, 'booking_codes': booking_codes})

def update_result(request, match_id, result):
    match = Match.objects.get(id=match_id)
    match.result = result
    match.save()
    return redirect('match_list1')

def vip_odds(request, odds_range):
    # Handling VIP odds range matches
    if odds_range == "2-5":
        vip_matches = Match.objects.filter(odds__gte=2.0, odds__lte=5.0, category='vip')
    elif odds_range == "5+":
        vip_matches = Match.objects.filter(odds__gte=5.0, category='vip')
    elif odds_range == "10+":
        vip_matches = Match.objects.filter(odds__gte=10.0, category='vip')
    elif odds_range == "20+":
        vip_matches = Match.objects.filter(odds__gte=20.0, category='vip')

    return render(request, 'vip_odds.html', {'matches': vip_matches, 'page_title': f'VIP Odds {odds_range}'})

def yesterdays_tips(request):
    # Matches from yesterday
    yesterday = date.today() - timedelta(days=1)
    yesterday_matches = Match.objects.filter(match_date=yesterday)
    return render(request, 'yesterdays_tips.html', {'matches': yesterday_matches, 'page_title': "Yesterday's Tips"})