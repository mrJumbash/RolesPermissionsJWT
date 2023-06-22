from django.contrib import admin
from django.db.models import QuerySet

from service.models import Review, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "price"]
    fields = ["title", "description", "price"]
    readonly_fields = ["id", "created_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "text", "rate", "product"]
    fields = ["text", "rate", "product"]
    raw_id_fields = ["product"]
    readonly_fields = ["created_at", "id"]

    def get_queryset(self, request) -> QuerySet[Review]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("product")
        return queryset
