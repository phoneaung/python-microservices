from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        # set product and specify the fields
        model = Product
        fields = "__all__"