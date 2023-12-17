import logging
from datetime import datetime

from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect

from factory.models import FactoryOwner
from account.models import Account
from reciepts.models import Receipts
from app.middleware import auth
from app.messages import globalMessage
from reciepts.validations import receipts_validation


logger = logging.getLogger('django')

# Create your views here.


class ReceiptsView(View):
    template_name = 'receipts.html'
    page_title = 'Receipts'
    """
       Retrive all receipts 
    """

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')

            try:
                receipts = Receipts.objects.filter(is_delete=False)

            except Receipts.DoesNotExist as exe:
                Exception(exe)

            content = {}
            content['page_title'] = self.page_title
            content['receipts'] = receipts
            return render(request, self.template_name, content)

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            return redirect('reciepts')


class ReceiptsAdd(View):
    template_name = 'addreceipts.html'
    page_title = 'Add Receipts'

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')

            try:
                owner = FactoryOwner.objects.filter(is_delete=False)
                account = Account.objects.filter(is_delete=False)

            except Account.DoesNotExist as exe:
                raise Exception(exe)

            content = {}
            content['page_title'] = self.page_title
            content['owners'] = owner
            content['accounts'] = account
            return render(request, self.template_name, content)

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            return redirect('receipts')

    def post(self, request):
        try:
            if not auth(request):
                return redirect('login')

            error_list, date, account_id, owner_id, amount = receipts_validation(
                request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('addReceipt')

            owner = FactoryOwner.objects.get(reference_id=owner_id)
            account = Account.objects.get(reference_id=account_id)

            Receipts.objects.create(date=date, mode_of_payment=account, owner=owner,
                                    amount=amount, created_at=datetime.now(), created_by=request.user)
            messages.success(request, globalMessage.SUCCESS_MSG)

            return redirect('addReceipt')

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.info(request, globalMessage.ERROR_MSG)
            return redirect('addReceipt')


class ReceiptsDetail(View):
    template_name = 'editreceipts.html'
    page_title = 'Edit Receipts'
    """ update, retrive data with reference id 
    """

    def get(self, request, ref_id):
        try:
            receipt = Receipts.objects.get(reference_id=ref_id)
            owners = FactoryOwner.objects.filter(is_delete=False)
            account = Account.objects.filter(is_delete=False)

        except Receipts.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['receipt'] = receipt
        content['owners'] = owners
        content['accounts'] = account
        return render(request, self.template_name, content)

    def post(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')

            error_list, date, account_id, owner_id, amount = receipts_validation(
                request)

            if not error_list:
                return redirect(request, error_list[0])

            account = Account.objects.get(reference_id=account_id)
            owner = FactoryOwner.objects.get(reference_id=owner_id)
            receipt = Receipts.objects.get(reference_id=ref_id)
            receipt.date = date
            receipt.mode_of_payment = account
            receipt.owner = owner
            receipt.amount = amount
            receipt.save()

            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('editreceipt')

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('receipts')


class ReceiptDelete(View):
    def delete(self, request, ref_id):
        try:
            Receipts.objects.get(reference_id=ref_id).delete()
            return JsonResponse({'msg': globalMessage.SUCCESS_MSG}, status=200)

        except Receipts.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)
            return JsonResponse({'msg': globalMessage.ERROR_MSG}, status=500)
