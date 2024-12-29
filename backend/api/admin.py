from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Product, ProductImage, Platform, Region, ActivationOption, ProductVariant

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "rating", "created_at", "updated_at", "main_image_preview")
    list_filter = ("created_at", "updated_at", "rating")
    search_fields = ("name", "description")
    ordering = ("-created_at",)
    readonly_fields = ("main_image_preview",)

    def main_image_preview(self, obj):
        if obj.main_image:
            return f'<img src="{obj.main_image.url}" style="max-height: 100px;" />'
        return "Нет изображения"
    main_image_preview.allow_tags = True
    main_image_preview.short_description = "Превью изображения"


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image") 
    search_fields = ("product__name",) 


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ("name",) 
    search_fields = ("name",)


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("name",) 
    search_fields = ("name",) 


@admin.register(ActivationOption)
class ActivationOptionAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ProductVariant)
class ProductVariantAdmin(admin.ModelAdmin):
    list_display = ("product", "platform", "activation_option", "region", "price") 
    list_filter = ("platform", "region", "activation_option") 
    search_fields = ("product__name", "region__name", "platform__name") 
    ordering = ("product__name",) 
    
class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff") 
    list_filter = ("is_staff", "is_superuser", "is_active") 
    search_fields = ("username", "email", "first_name", "last_name") 
    ordering = ("username",) 
    
admin.site.unregister(User) 
admin.site.register(User, CustomUserAdmin)
