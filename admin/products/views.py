from rest_framework import viewsets
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ViewSet):
    # /api/products/<str:id> 
    def list(self, request):
        # import all the products and view here
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        
        return Response(serializer.data)

    def create(self, request): 
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass 

    def destroy(self, request, pk=None):
        pass