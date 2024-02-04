from rest_framework import viewsets

class ProductViewSet(viewsets.ViewSet):
    # /api/products/<str:id> 
    def list(self, request):
        # import all the products and view here
        pass

    def create(self, request): 
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass 

    def destroy(self, request, pk=None):
        pass