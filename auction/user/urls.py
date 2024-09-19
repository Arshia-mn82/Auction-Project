from django.urls import path
from .views import *
urlpatterns = [
    path('create-auction/', CreateAuction.as_view()),
    path('delete-auction/' , DeleteAuction.as_view()),
    path('finished-products/' , FinishedProducts.as_view()),
    
]