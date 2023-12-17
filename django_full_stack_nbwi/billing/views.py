import logging
from datetime import datetime
from django.db import IntegrityError, transaction
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views import View
from billing.validation import invoiceValidation
from billing.models import Transaction, TransactionDetail
from account.models import Account
from group.models import Group
from item.models import Item
from rates.models import Rates
from factory.models import Factory
from app.messages import globalMessage
from app.middleware import auth

# Create your views here.

logger = logging.getLogger('django')


class BillingView(View):
    template_name = 'invoice.html'
    page_title = "Invoice"

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')

            try:
                rates = Rates.objects.filter(is_delete=False)
                factories = Factory.objects.filter(is_delete=False)
                accounts = Account.objects.filter(is_delete=False)
                groups = Group.objects.filter(is_delete=False)

            except Group.DoesNotExist as exe:
                logger.error(str(exe), exc_info=True)
                raise Exception(exe)

            content = {}
            content['page_title'] = self.page_title
            content['rates'] = rates if rates else ''
            content['accounts'] = accounts if accounts else ''
            content['factories'] = factories if factories else ''
            content['groups'] = groups if groups else ''
            return render(request, self.template_name, content)

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('billing')

    def post(self, request):
        try:
            data = request.POST
            ref_no = data.get('ref_no')
            date = data.get('date')
            factory_id = data.get('factory_id')
            group_id = data.getlist('group_id')
            item_id = data.getlist('item_id')
            account_id = data.get('account_id')
            # item_unit = data.getlist('item_unit')
            item_qty = data.getlist('item_qty')
            rates = data.getlist('rates')
            vehicle_rent = data.getlist('vehicle_rent')
            product_charge = data.getlist('product_charge')
            wrapping = data.getlist('wrapping')
            label_charge = data.getlist('label_charge')
            total_amount = data.get('total_amount')
            total_recevied = data.get('total_recevied')
            total_product_charge = data.get('total_product_charge')
            total_vehicle_rent = data.get('total_vehicle_rent')
            total_label_charge = data.get('total_label_charge')
            total_wrapping = data.get('total_wrapping')

            error_list = invoiceValidation(request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('invoice')

             # geting model with id
            user = User.objects.first()
            factory = Factory.objects.get(id=factory_id)
            account = Account.objects.get(id=account_id)

            with transaction.atomic():
                sid = transaction.savepoint()  # creating save id 
                try:
                    _transactions = Transaction.objects.create(ref_no=ref_no, date=date, factory_id=factory, total_amount=total_amount,
                                                               amount_received=total_recevied, total_vehicle_rent=total_vehicle_rent, total_label_charge=total_label_charge,
                                                               total_wrapping=total_wrapping, total_product_charge=total_product_charge,
                                                               account_id=account, created_at=datetime.now(), created_by=user)

                    for index in range(len(item_id)):
                        group = Group.objects.get(id=group_id[index])
                        item = Item.objects.get(id=item_id[index])
                        TransactionDetail.objects.create(group_id=group, item_id=item,
                                                         item_qty=item_qty[index], item_rate=rates[
                                                             index], vehicle_rent=vehicle_rent[index],
                                                         product_charge=product_charge[
                                                             index], label_charge=label_charge[index],
                                                         wrapping=wrapping[index], transaction_id=_transactions.id,
                                                         created_at=datetime.now(), created_by=user)
                    transaction.savepoint_commit(sid)
                    messages.success(request, "Data is save successfully.")
                except IntegrityError as exe:
                    transaction.savepoint_rollback(sid)
                    raise Exception(exe)

                return redirect('invoice')

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            print(exe)
            return redirect('invoice')


class PrintInvoice(View):
    template_name = 'invoice-print.html'
    page_title = 'Print'

    def get(self, request):
        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)
