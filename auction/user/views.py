from .models import *
from .serializers import *
from rest_framework.views import APIView
from datetime import datetime
from django.http.response import JsonResponse


class CheckOffer(APIView):
    def post(request, self):
        data = request.data
        product_id = data.get("product_id")
        customer_id = data.get("customer_id")
        price = data.get("price")

        finded_product = Product.objects.get(id=product_id)

        if (
            finded_product.start_time <= datetime.now()
            and finded_product.end_time >= datetime.now()
            and price > finded_product.highest_price
        ):
            Offer.objects.create(
                product=product_id,
                customer=customer_id,
                price=price,
                date=datetime.now(),
            )
            time_change = datetime.timedelta(minutes=10)
            finded_product.end_time = finded_product.end_time + time_change
            finded_product.highest_price = price
            finded_product.save()
            return JsonResponse("Offer Created", safe=False)

        else:
            return JsonResponse("Not valid Time or Price", safe=False)

