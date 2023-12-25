from rest_framework import serializers
from .models import Budget
from category.serializers import CategorySerializer


class BudgetSerializer(serializers.ModelSerializer):
    """
    Budget serializer
    """

    category = CategorySerializer(read_only=True)
    start_date = serializers.DateField(input_formats=["%Y-%m", "%Y-%m-%d"], format="%Y-%m")


    class Meta:
        model = Budget
        fields = ("id", "category", "amount", "currency", "start_date", "user")
        read_only_fields = ("id", "user")
