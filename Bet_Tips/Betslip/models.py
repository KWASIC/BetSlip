# tips/models.py
from django.db import models

# tips/models.py

from django.db import models
from datetime import date

class Match(models.Model):
    CATEGORY_CHOICES = [
        ('regular', 'Regular'),
        ('vip', 'VIP'),
        ('correct_score', 'Correct Score'),
        ('yesterday', 'Yesterday'),
    ]

    team_1 = models.CharField(max_length=100)
    team_2 = models.CharField(max_length=100)
    match_date = models.DateField()
    odds = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)  # Add odds field
    selection = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='regular')
    result = models.CharField(max_length=10, choices=[('win', '✅'), ('lose', '❌'), ('pending', 'Pending')], default='pending')

    def __str__(self):
        return f"{self.team_1} vs {self.team_2} on {self.match_date}"

    @property
    def is_yesterday(self):
        return self.match_date == (date.today() - timedelta(days=1))


class BookingCode(models.Model):
    site_name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.site_name
