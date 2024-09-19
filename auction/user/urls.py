from django.urls import path
from .views import *

urlpatterns = [
    path("create-auction/", CreateAuction.as_view()),
    path("delete-auction/", DeleteAuction.as_view()),
    path("finished-products/", FinishedProducts.as_view()),
    path("add-offer/", CheckOffer.as_view()),
    path('login/' , Login.as_view()),
    path('refresh/' , Refresh.as_view()),
    path('create-provider/' , CreateProvider.as_view()),
    path('create-product/' , CreateProduct.as_view()),
    path('create-customer/' , CreateCustomer.as_view()),
    path('offers/' , DetailOffer.as_view())
]
