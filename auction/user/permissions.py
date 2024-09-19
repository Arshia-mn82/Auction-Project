from rest_framework.permissions import BasePermission
from .models import *

class IsCustomer(BasePermission):
    def has_permission(self, request, view):
        customer = Customer.objects.get(user=request.user)
        if customer:
            return True
        else:
            return False
        
class IsProvider(BasePermission):
    def has_permission(self, request, view):
        provider = Provider.objects.get(user=request.user)
        if provider:
            return True
        else:
            return False