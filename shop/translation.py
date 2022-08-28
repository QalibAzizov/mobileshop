from modeltranslation.translator import translator, TranslationOptions
from shop.models import *

class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')

translator.register(Category, CategoryTranslationOptions)


class BrandTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')

translator.register(Brand, BrandTranslationOptions)


class DiscountTranslationOptions(TranslationOptions):
    fields = ('title', 'slug')

translator.register(Discount, DiscountTranslationOptions)


class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)

translator.register(Product, ProductTranslationOptions)