from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
    """
    This model represents an expense in the app. 
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    

    currency_choices = [ 
        ('GBP', 'GBP'), 
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('CHF', 'CHF'),
        ('JPY', 'JPY'),
        ('CAD', 'CAD'),
        ('AUD', 'AUD'),
    ]

    currency = models.CharField(max_length=3, choices=currency_choices, default='GBP')

    amount = models.DecimalField( max_digits=10, decimal_places=2)

    created_on = models.DateTimeField(auto_now_add=True)

    class Meta: 
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.item} | by {self.user}"

