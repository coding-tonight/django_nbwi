import logging
from datetime import datetime

from django.views import View
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.contrib import messages

from item.models import Item
from item.validation import itemValidation
from app.middleware import auth
from app.messages import globalMessage

# Create your views here.

logger = logging.getLogger('django')

class ItemView(View):
    template_name = 'itemtable.html'
    page_title = 'Inventory'
    success_url = 'item'

    def get(self, request):  # check if user is auth or not
        if not auth(request):
            return redirect('login')
        
        try:
            items = Item.objects.filter(is_delete=False)

        except Item.DoesNotExist as exe:
            logger.error(exe)
            items = ''

        content = {}
        content['page_title'] = self.page_title
        content['items'] = items
        return render(request, self.template_name, content)


class ItemAdd(View):
    template_name = 'additem.html'
    page_title = 'Add Item'
    success_url = 'item'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        
        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)

    def post(self, request):
        try:
            if not auth(request):
                return redirect('login')
            
            error_list, item_name, item_code, item_qty,  item_unit, item_code, item_opening, item_purchase_rate ,item_type = itemValidation(
                request)
            if error_list:
                messages.error(request, 'invalid input')
                return redirect('item')
            Item.objects.create(item_name=item_name, item_code=item_code, item_qty=item_qty, item_type=item_type,
                                item_unit=item_unit, opening_stock=item_opening, purchase_rate=item_purchase_rate, created_at=datetime.now())
            return redirect('item')
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, 'Ops something went wrong.')
            return redirect('item')


class ItemDetail(View):
    template_name = 'edititem.html'
    page_title = 'Edit Item'

    """ retrive data with reference and update 
    """
    def get(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')
            
            #  get item with reference id 
            try:
                item = Item.objects.get(reference_id=ref_id)
            
            except Item.DoesNotExist as exe:
                raise Exception(exe)
            
            content = {}
            content['page_title'] = self.page_title
            content['item'] = item if item else ''
            return render(request, self.template_name, content)
        
        except Exception as exe:
            logger.error(str(exe) , exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('item')
    

    def post(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')
            
            error_list, item_name, item_code, item_qty,  item_unit, item_code, item_opening, item_purchase_rate, item_type = itemValidation(
                    request)
            # validating the fields
            if error_list:
                messages.error(request, 'invalid input')
                return redirect('item')
            
            item = Item.objects.get(reference_id=ref_id)
            item.item_name = item_name
            item.item_code = item_code 
            item.item_qty = item_qty
            item.item_unit = item_unit
            item.purchase_rate = item_purchase_rate
            item.opening_stock = item_opening
            item.item_type = item_type
            item.updated_at = datetime.now()
            item.updated_by = request.user
            item.save()
            
            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('item')
         
        except Item.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            return redirect('item')
        

class ItemDelete(View):
    """ delete item view
    """
    def delete(self, request, ref_id):
        try:
            Item.objects.filter(reference_id=ref_id).update(is_delete=True)
            return JsonResponse({globalMessage.SUCCESS_MSG: globalMessage.SUCCESS_RESPONSE}, status=200)
        
        except Item.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            return JsonResponse({globalMessage.ERROR_MSG: globalMessage.ERROR_RESPONSE}, status=500)
    
        
        
