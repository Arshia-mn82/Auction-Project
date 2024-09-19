from rest_framework.serializers import ModelSerializer
from .models import *

class productSerilizer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
        
class CustomerSerilizer(ModelSerializer):

    class Meta:
        model = Customer
        fields = "__all__"
        
class ProviderSerilizer(ModelSerializer):

    class Meta:
        model = Provider
        fields = "__all__"
        


class OfferSerilizer(ModelSerializer):

    class Meta:
        model = Offer
        fields = "__all__"
        
class AuctionsSerilizer(ModelSerializer):

    class Meta:
        model = Auctions
        fields = "__all__"