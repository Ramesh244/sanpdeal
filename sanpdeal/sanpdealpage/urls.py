from django.urls import path 

from . import views 


urlpatterns = [
    path('singup',views.signingup,name="sin"),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('',views.Home,name="homepage"),
    path('about',views.about,name="aboutpage"),
    path('contact',views.contact,name="contactpage"),
    path('store',views.store,name="storepage"),
    path('cart',views.cart,name="cartpage"),
    path('check',views.Checkout,name="checkpage"),
    path('details',views.detialsform,name="detailspage"),
    path('delete/<int:id>/', views.deletedata, name="deleting"),
    path('details/<int:id>/', views.updatedata, name="updating")
   
]
