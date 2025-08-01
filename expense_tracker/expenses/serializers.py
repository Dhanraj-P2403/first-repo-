from rest_framework import serializers
from .models import Expense

class Expenseserializers(serializers.ModelSerializer):
    class meta:
        model=Expense
        fields='__all__'
        