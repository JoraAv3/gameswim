from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название товара")
    description = models.TextField(verbose_name="Описание товара")
    rating = models.FloatField(default=0.0, verbose_name="Рейтинг товара")
    main_image = models.ImageField(upload_to="product_main_images/", null=True, blank=True, verbose_name="Основное изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return self.name



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="product_images/", verbose_name="Изображение")

    def __str__(self):
        return f"Image for {self.product.name}"


class Platform(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название платформы")

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Название региона")
    def __str__(self):
        return self.name


class ActivationOption(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Вариант активации")

    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variants")
    platform = models.ForeignKey(Platform, on_delete=models.CASCADE, verbose_name="Платформа")
    activation_option = models.ForeignKey(
        ActivationOption, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Вариант активации"
    )
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Регион")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return f"{self.product.name} - {self.platform.name} - {self.activation_option} - {self.region.name}"


class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wallet", verbose_name="Пользователь")
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, verbose_name="Баланс")
    currency = models.CharField(max_length=10, default="RUB", verbose_name="Валюта")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")

    def __str__(self):
        return f"Кошелёк пользователя {self.user.username} с балансом {self.balance} {self.currency}"