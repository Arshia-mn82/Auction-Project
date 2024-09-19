from .models import *
from .serializer import *
from rest_framework.views import APIView
import datetime
from django.http.response import JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView , ListAPIView
import json
from .permissions import *
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from datetime import timedelta



class Login(TokenObtainPairView):
    pass

class Refresh(TokenObtainPairView):
    pass


class CheckOffer(APIView):
    def post(self, request):
        data = json.loads(request.body)
        product_id = data["product_id"]
        customer_id = data["customer_id"]
        price = data["price"]
        finded_customer = Customer.objects.get(id = customer_id)
        finded_product = Product.objects.get(id=product_id)
        naive_start_time = finded_product.start_time.replace(tzinfo=None)
        naive_end_time = finded_product.end_time.replace(tzinfo=None)
        if (
            naive_start_time <= datetime.datetime.now()
            and naive_end_time >= datetime.datetime.now()
            and price > finded_product.highest_price
        ):
            Offer.objects.create(
                product=finded_product,
                customer=finded_customer,
                price=price,
                date=datetime.datetime.now(),
            )
            time_change = datetime.timedelta(minutes=10)
            finded_product.end_time = finded_product.end_time + time_change
            finded_product.highest_price = price
            finded_product.save()
            return JsonResponse("Offer Created", safe=False)

        else:
            return JsonResponse("Not valid Time or Price", safe=False)


class CreateAuction(ListCreateAPIView):
    queryset = Auctions.objects.all()
    serializer_class = AuctionsSerilizer
    permission_classes = [IsProvider]
    

class CreateProvider(ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerilizer
    
    
class DeleteAuction(RetrieveUpdateDestroyAPIView):
    queryset = Auctions.objects.all()
    serializer_class = AuctionsSerilizer
    permission_classes = [IsProvider]


class FinishedProducts(APIView):
    def get(self, request):
        finished_products = Product.objects.filter(end_time__lt=datetime.now())
        finished_products = json.dumps(finished_products)
        return JsonResponse(finished_products, safe=False)
    
class CreateProduct(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerilizer
    permission_classes = [IsProvider]
    
class CreateCustomer(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerilizer

class DetailOffer(ListAPIView):
    queryset = Offer.objects.all()
    serializer_class = OfferSerilizer
