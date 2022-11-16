
from .models import DetailsForm

from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import * 

class Detailsaboutpage(forms.ModelForm):
    class Meta:
        model= DetailsForm
        fields=['name_of_product','price_of_product','manufature_of_product','rating','reviews']





# class CustomerForm(forms.ModelForm):

#     class Meta:

#         model=Customer

#         fields='__all__'


# class ProductForm(forms.ModelForm):

#     class Meta:

#         model=Product

#         fields=['name','price']

# class RatingForm(forms.ModelForm):

#     class Meta:

#         model=Rating

#         fields='__all__'

# class OrderForm(forms.ModelForm):

#     class Meta:

#         model=Order

#         fields='__all__'

# class OrderItemItem(forms.ModelForm):

#     class Meta:

#         model=OrderItem

#         fields='__all__'

# class ShippingAddForm(forms.ModelForm):

#     class Meta:

#         model=ShippingAdd

#         fields='__all__'

    
class Contact_us(forms.ModelForm):

    class Meta:

        model=Contact

        fields='__all__'



class Singup(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput)
    class Meta:
        model= User
        
        fields=['username', 'first_name', 'last_name','email']
        Widget={'password':forms.PasswordInput}