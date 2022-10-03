
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class AbsrtactModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Contact(AbsrtactModel):
    first_name = models.CharField('Ad',max_length=50)
    last_name = models.CharField('Soyad',max_length=50)
    email = models.EmailField('E Pocht',max_length=40)
    adress = models.CharField("Adress ",max_length=1024)
    phone = models.CharField('Telefon',max_length=20)


    def __str__(self) :
        return self.first_name

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'  


class Category(AbsrtactModel):
    title = models.CharField('category_name',max_length=100, db_index=True)
    slug = models.SlugField( max_length=255, db_index=True, editable=False)
    cover_image = models.ImageField(upload_to = 'cateqory/',null = True, blank=True )


    def __str__(self):
        return (self.title)

    @property
    def product_count(self):
        return self.product_categories.count()

    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'



class Brand(AbsrtactModel):
    title = models.CharField('brand',max_length=100, db_index=True)
    slug = models.SlugField( max_length=255, db_index=True, editable=False)


    def __str__(self):
        return (self.title)

    @property
    def product_count(self):
        return self.product_brands.count()

    
    class Meta:
        verbose_name = 'brand'
        verbose_name_plural = 'brands'


class Discount(AbsrtactModel):
    title = models.CharField(max_length=100)
    slug = models.SlugField( max_length=255, db_index=True, editable=False)
    percentage = models.IntegerField()

    def __str__(self):
        return (self.title)

    
    class Meta:
        verbose_name = 'discount'
        verbose_name_plural = 'discounts'



class Product(AbsrtactModel):
    category = models.ForeignKey(Category, related_name='product_categories', on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, related_name='product_brands', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product/")
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField( max_length=255, db_index=True, editable=False)

    code = models.IntegerField()
    price = models.IntegerField(null = True, blank=True)
    sellprice = models.IntegerField()
    description = models.TextField('description')
    discount = models.ForeignKey(Discount, related_name='discount', on_delete=models.CASCADE, null = True, blank=True)


    def get_absolute_url(self):
        return reverse_lazy('product', kwargs={
            'slug' : self.slug
        })


    def __str__(self):
        return (self.title)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'



class Image(AbsrtactModel):
    productversion= models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")
    is_main = models.BooleanField(default=False)


    def __str__(self):
        return (self.productversion.title)
