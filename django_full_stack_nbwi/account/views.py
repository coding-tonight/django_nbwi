import logging
from datetime import datetime

from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, redirect

from account.models import Account
from app.messages import globalMessage
from app.middleware import auth



# Create your views here.

logger = logging.getLogger('django')


class AccountView(View):
    template_name = 'account.html'
    page_title = 'Account'

    def get(self, request):
        if not auth(request):  # if user exist or not
            return redirect('login')
        
        try:
            accounts = Account.objects.filter(is_delete=False)
        except Account.DoesNotExist as exe:
            logging.error(exe)
            accounts = ''

        content = {}
        content['page_title'] = self.page_title
        content['accounts'] = accounts
        return render(request, self.template_name, content)


class AccountAdd(View):
    template_name = 'addaccount.html'
    page_title = 'Add Account'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        
        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)

    def post(self, request):
        if not auth(request):
            return redirect('login')
        
        data = request.POST
        account_name = data.get('account_name')
        account_number = data.get('account_number')
        opening_balance = data.get('opening_balance') if data.get(
            'opening_balance') else 0

        Account.objects.create(account_name=account_name, account_number=account_number,
                               opening_balance=opening_balance, created_at=datetime.now())

        return redirect('account')


class AccountDetail(View):
    template_name = 'editaccount.html'
    page_title = 'Edit Account'

    def get(self, request, ref_id):
        if not auth(request):
            return redirect('login')
        
        try:
            account = Account.objects.get(reference_id=ref_id)
        except Account.DoesNotExist as exe:
            logging.error(exe)
            account = ''

        content = {}
        content['page_title'] = self.page_title
        content['account'] = account
        return render(request, self.template_name, content)

    def post(self, request, ref_id):
        if not auth(request):
            return redirect('login')
        
        data = request.POST
        account_name = data.get('account_name')
        account_number = data.get('account_number')
        opening_balance = data.get('opening_balance') if data.get(
            'opening_balance') else 0

        Account.objects.filter(reference_id=ref_id).update(account_name=account_name, account_number=account_number,
                                             opening_balance=opening_balance, created_at=datetime.now())

        return redirect('account')
    

class AccountDelete(View):
    def delete(self, request, ref_id):
        try:
            Account.objects.filter(reference_id=ref_id).update(is_delete=True)
            return JsonResponse({globalMessage.SUCCESS_RESPONSE: globalMessage.SUCCESS_MSG} , status=200)
        except Account.DoesNotExist as exe:
            logger.error(exe)
            return JsonResponse({globalMessage.ERROR_RESPONSE: globalMessage.ERROR_MSG} , status=400)


