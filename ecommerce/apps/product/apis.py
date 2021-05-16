from .models import Category,SubCategory,Product
from rest_framework import viewsets, permissions

from .serializers import CategorySerializer, SubCategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permissions = [
        permissions.AllowAny
    ]
    serializer_class = CategorySerializer