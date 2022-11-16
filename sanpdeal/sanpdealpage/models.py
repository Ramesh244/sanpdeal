
from django.db import models

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, MaxValueValidator


class DetailsForm(models.Model):
    name_of_product=models.CharField(max_length=150)
    price_of_product=models.CharField(max_length=150)
    manufature_of_product=models.CharField(max_length=150)
    rating=models.IntegerField()
    reviews=models.CharField(max_length=150)

class Contact(models.Model):

    name=models.CharField(max_length=80)

    email=models.EmailField(max_length=80)

    issue=models.CharField(max_length=500)


class Sinup(models.Model):
    FirstName = models.CharField(max_length=100)
    Lastname= models.CharField(max_length=100)
    age = models.IntegerField()
    email= models.CharField(max_length=100)
    password=models.CharField(max_length=100)

class Customer(models.Model):
    User = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

    def __str__(self):
        return self.name


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    # img = models.ImageField(upload_to='productImage')
    description = models.TextField()
    price = models.FloatField()
    review = models.TextField()
    image=models.ImageField()

    def imageUrl(self):
        try:
            url=self.image.url
        except:
            url=""
        return url

    # def no_of_rating(self):
    #     rating = Rating.objects.filter(product=self)
    #     return len(rating)

    # def avg_rating(self):
    #     sum = 0
    #     ratings = Rating.objects.filter(self)
    #     for rating in ratings:
    #         sum += rating
    #         if len(ratings>0):
    #             return sum//len(rating)
    #         else:
    #             return 0  

    def __str__(self):
        return self.name



class Rating(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self):
        return str(self.product)+"---"+str(self.user)




# class Product(models.Model):
#   title = models.CharField(max_length=255)

#   slug = models.SlugField(null=False, unique=True)

      
#   def myrating(self):
#      myvalue = self.ratingproduct.aggregate(Avg('rating'))
#      return myvalue

# class Review(models.Model):
#    fullname = models.CharField(max_length=200)
#    rating = models.IntegerField()
#    product = models.ForeignKey(Product, related_name="ratingproduct", 
#              on_delete=models.CASCADE, blank=True, null=True)

#    def __str__(self):
#        return self.fullname


class Order(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True)
    date_orderd=models.DateTimeField(auto_now_add=True)
    complete=models.BooleanField(default=False,blank=False)
    Transaction_Id=models.CharField(max_length=200)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE,blank=True)
    Order=models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    quanatity=models.IntegerField(default=0,blank=True)
    date_added=models.DateTimeField(auto_now_add=True)


class ShippingAdd(models.Model):
    Customer=models.ForeignKey(Customer,on_delete=models.CASCADE,blank=True)
    Order=models.ForeignKey(Order,on_delete=models.CASCADE,blank=True)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=300)
    state=models.CharField(max_length=300)
    pincode=models.IntegerField(validators=[MaxValueValidator(6)])
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

    
