from django.contrib import admin

# Register your models here.
# tips/admin.py

from django.contrib import admin
from .models import Match, BookingCode


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('team_1', 'team_2', 'match_date', 'category', 'odds', 'selection', 'result')
    list_filter = ('match_date', 'category', 'result')
    search_fields = ('team_1', 'team_2')
    

admin.site.register(BookingCode)
