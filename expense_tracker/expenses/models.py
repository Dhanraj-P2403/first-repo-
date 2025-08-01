from django.db import models

class Expense(models.Model):
    title=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=20 , decimal_places=2)
    category=models.CharField(max_length=100)
    date=models.DateField()

def __str__(self):
    return f"{self.title}-{self.price}"
