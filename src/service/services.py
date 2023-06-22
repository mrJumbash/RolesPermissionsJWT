from service.models import Product, Review
from django.db.models import Avg


class ProductService:
    __product_model = Product

    @classmethod
    def get_list(cls, **kwargs):
        return (
            cls.__product_model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "description", "price")
        )


class ReviewService:
    __review_model = Review

    @classmethod
    def get_list(cls, **kwargs):
        return (
            cls.__review_model.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "text", "rate", "product_id")
        )
