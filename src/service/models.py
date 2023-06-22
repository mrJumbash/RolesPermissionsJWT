from django.db import models
from common.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator
from service.settings import RATE_CHOICES


class Product(BaseModel):
    price = models.FloatField(
        verbose_name="Цена", default=0, validators=[MinValueValidator(0)]
    )
    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return f"{self.title} - {self.price}"


class Review(BaseModel):
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="product_reviews"
    )
    text = models.TextField(verbose_name="Отзыв")
    rate = models.PositiveSmallIntegerField(
        choices=RATE_CHOICES,
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return f"{self.product} - {self.rate}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
