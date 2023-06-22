from django.shortcuts import render, redirect
from rest_framework import generics
from service.serializers import ProductSerializer, ReviewSerializer
from service.services import ProductService, ReviewService
from rest_framework.pagination import PageNumberPagination


class ProductAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = ProductService.get_list(is_deleted=False)
    pagination_class = PageNumberPagination


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = ProductService.get_list(is_deleted=False)
    pagination_class = PageNumberPagination
    lookup_field = "id"


class ReviewAPIView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    queryset = ReviewService.get_list(is_deleted=False)
    pagination_class = PageNumberPagination
