from service.models import Product
from django.db.models import Avg


class ProductReviewsStatistic:
    @staticmethod
    def get_labels():
        reviews = Product.objects.order_by("-created_at")[:5]
        return [review.title for review in reviews]

    @staticmethod
    def get_data():
        products = Product.objects.order_by("-created_at")[:5]
        return [
            product.product_reviews.aggregate(avg_rating=Avg("rate")).get("avg_rating")
            for product in products
        ]
