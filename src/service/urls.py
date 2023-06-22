from django.urls import path
from service.views.service_views import (
    ProductAPIView,
    ProductDetailAPIView,
    ReviewAPIView,
)

urlpatterns = [
    path("products/", view=ProductAPIView.as_view(), name="products"),
    path(
        "products/<uuid:id>/",
        view=ProductDetailAPIView.as_view(),
        name="product-detail",
    ),
    path("reviews/", view=ReviewAPIView.as_view()),
]
