import logging 
from datetime import datetime 

from django.contrib import messages
from django.shortcuts import render , redirect

from django.views import View
from payment.models import Payment
from account.models import Account 
from factory.models import FactoryOwner
from payment.validation import paymentValidation
from app.middleware import auth

# Create your views here.

logger = logging.getLogger('django')

class PaymentView(View):
    template_name = 'payment.html'
    page_title = 'Payment'

    def get(self, request):
        if not auth(request): # check if user is login or not
            return redirect('login')
        
        try:
            payment = Payment.objects.filter(is_delete=False)
        
        except Payment.DoesNotExist as exe:
            logger.error(str(exe) ,exc_info=True)
            payment = ''

        content = {}
        content['page_title'] = self.page_title
        content['payments'] = payment
        return render(request, self.template_name, content)


class PaymentAdd(View):
    template_name = 'addpayment.html'
    page_title = 'Payment Voucher'

    def get(self ,request):
        if not auth:  
            return redirect('login')
        
        try:
            owners = FactoryOwner.objects.filter(is_delete=False)
            accounts = Account.objects.filter(is_delete=False)
        except FactoryOwner.DoesNotExist as exe:
            logger.error(str(exe) , exc_info=True)
            owners = ''
            accounts = ''

        content = {}
        content['page_title'] = self.page_title
        content['owners'] = owners
        content['accounts'] = accounts
        return render(request , self.template_name, content)
     
    def post(self, request):
         if not auth:
             return redirect('login')
         
         try:
            error_list , date, owner_id, account_id ,amount = paymentValidation(request)
            if error_list:
                return redirect('addpayment')
            
            owner = FactoryOwner.objects.get(reference_id=owner_id)
            acocunt = Account.objects.get(reference_id=account_id)

            Payment.objects.create(date=date, owner_id=owner.id, mode_of_payment=acocunt, amount=amount , created_at=datetime.now())
            messages.success(request, 'Successfully added!')
            return redirect(request.path)
        
         except Payment.DoesNotExist as exe:
             logger.error(str(exe), exc_info=True)
             messages.success(request, 'Successfully added!')
             return redirect(request.path)

    



class PaymentDetail(View):
    template_name = 'editpayment.html'
    page_title  = 'Edit Payment'

    def get(self, request, ref_id):
        if not auth(request):  # this should be replace with different way to check the if user is validate or not
            return redirect('login')
        
        try:
            payments = Payment.objects.get(reference_id=ref_id)
            owners = FactoryOwner.objects.filter(is_delete=False)
            accounts = Account.objects.filter(is_delete=False)

        except FactoryOwner.DoesNotExist as exe:
            logger.error(str(exe) , exc_info=True)
            
            
        content = {}
        content['page_title'] = self.page_title
        content['owners'] = owners if owners else ''
        content['accounts'] = accounts if accounts else ''
        content['payment'] = payments if accounts else ''
        return render(request, self.template_name, content)
        

        
    