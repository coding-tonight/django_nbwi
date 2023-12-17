import logging
from datetime import datetime
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.views import View
from django.contrib import messages
from rates.models import Rates
from item.models import Item
from group.models import Group
from rates.validation import rateValidation
from app.messages import globalMessage
from app.middleware import auth
# Create your views here.

logger = logging.getLogger('django')

class RateView(View):
    template_name = 'rates.html'
    page_title = 'Rates'

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')
            
            try:
                rates = Rates.objects.filter(is_delete=False)

            except Rates.DoesNotExist as exe:
                logging.error(exe)

            content = {}
            content['page_title'] = self.page_title
            content['rates'] = rates if rates else ''
            return render(request, self.template_name, content)
        
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request,globalMessage.ERROR_MSG)
            return redirect('rates')


class RateAdd(View):
    template_name = 'addrate.html'
    page_title = "Add Rates"

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')
            try:
                items = Item.objects.filter(is_delete=False)
                groups = Group.objects.filter(is_delete=False)
            except Item.DoesNotExist as exe:
                logging.error(exe)

            content = {}
            content['page_title'] = self.page_title
            content['items'] = items if items else ''
            content['groups'] = groups if groups else ''
            return render(request, self.template_name, content)
        
        except Exception as exe:
            logger.error(str(exe) ,exc_info=True)
            return redirect(request.path)

    def post(self, request):
        try:
            if not auth(request):
                return redirect('login')
            
            error_list, group_id, item_id, sale_rate, product_charge, wrapping, vehicle_rent , label_charge = rateValidation(
                request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('addRate')
            
            
            group = Group.objects.get(id=group_id)
            item = Item.objects.get(id=item_id)
            Rates.objects.create(group_id=group, item_id=item, sale_rate=sale_rate, vehicle_rent=vehicle_rent,
                                product_charge=product_charge, wrapping=wrapping , label_charge=label_charge, created_at=datetime.now())
            messages.success(request, globalMessage.SUCCESS_MSG)

            return redirect('addRate')
        
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('addRate')


class RateDetail(View):
    template_name = 'editrate.html'
    page_title = 'Edit Rate'

    def get(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')
            
            try:
                rate = Rates.objects.get(reference_id=ref_id)
                items = Item.objects.filter(is_delete=False)
                groups = Group.objects.filter(is_delete=False)

            except Rates.DoesNotExist as exe:
                raise Exception(exe)

            content = {}
            content['page_title'] = self.page_title
            content['rate'] = rate if rate else ''
            content['items'] = items if items else ''
            content['groups'] = groups if groups else ''
            return render(request, self.template_name, content)
        
        except Exception as exe:
            logger.error(str(exe) ,exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('rates')

    def post(self, request, ref_id):
        try:
            error_list, group_id, item_id, sale_rate, product_charge, wrapping, vehicle_rent ,label_charge = rateValidation(
                request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect(request.path)

            group = Group.objects.get(id=group_id)
            item = Item.objects.get(id=item_id)
            Rates.objects.filter(reference_id=ref_id).update(group_id=group, item_id=item, sale_rate=sale_rate, vehicle_rent=vehicle_rent,
                                            product_charge=product_charge, wrapping=wrapping, label_charge=label_charge ,
                                            updated_at=datetime.now(), updated_by=request.user)
            
            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('rates')
        
        except Exception as exe:
            logger.error(str(exe) , exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('rates')


class RateDelete(View):
    def delete(self, request , ref_id):
        try:
            Rates.objects.filter(reference_id=ref_id).update(is_delete=True ,updated_at=datetime.now(),updated_by=request.user)
            return JsonResponse({ globalMessage.SUCCESS_RESPONSE: globalMessage.SUCCESS_MSG }, status=200)
        
        except Rates.DoesNotExist as exe:
            logger.error(str(exe) , exc_info=True)
            return JsonResponse({ globalMessage.ERROR_RESPONSE: globalMessage.ERROR_MSG } ,status=400)
