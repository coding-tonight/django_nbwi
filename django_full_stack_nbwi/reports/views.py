import logging

from django.views import View
from django.shortcuts import render ,redirect
from billing.models import Transaction , TransactionDetail

from payment.models import Payment
from factory.models import Factory 
from item.models import Item
from app.middleware import auth
from app.nepaliCalendar import today_date , first_day_of_the_month_year
from reports.connection import sql_connection


# Create your views here.

logger = logging.getLogger('django')


class SaleOptionView(View):
    template_name = 'reports_options.html'
    page_title = 'Reports'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)

class SaleReportView(View):
    template_name = 'sales/sales_report.html'
    page_title = 'Sales Report'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        # only run task  if user is authenticated
        try:
            transactions = Transaction.objects.filter(is_delete=False)
        except Transaction.DoesNotExist as exe:
            logger.error(str(exe) ,exc_info=True)
            transactions = ''
              
        content ={}
        content['page_title'] = self.page_title
        content['transactions'] = transactions
        return render(request, self.template_name, content)
    




class LedgerReportView(View):
    template_name = 'ledger/ledger_report.html'
    page_title = 'Ledger Report'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        
        try:
           factories = Factory.objects.filter(is_delete=False)

        except Factory.DoesNotExist as exe:
            logger.error(str(exe) , exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['factories'] = factories if factories else ''
        return render(request, self.template_name, content)
    

class LedgerDetail(View):
    template_name = 'ledger/ledger_detail.html'
    page_title = 'Ledger Detail'

    def get(self, request, ref_id):
        if not auth(request):
            return redirect('login')
        
        try:
            factory = Factory.objects.get(reference_id=ref_id)
            transactions = Transaction.objects.filter(is_delete=False, factory_id=factory.id)
            payments = Payment.objects.filter(is_delete=False, owner_id=factory.owner_id)

        except Exception as exe:
            logger.error(str(exe) , exc_info=True)
            
        content = {}
        content['page_title'] = self.page_title
        content['transactions'] = transactions  if transactions else ''
        content['payments'] = payments if payments else ''
        return render(request, self.template_name ,content)
    



class InventoryWiseView(View):
    template_name = 'sales/item_wise.html'
    page_title = 'Item Wise Sale Report'
    
    # redirect to login page if user is not authenticated
    def get(self, request):
        if not auth(request):
            return redirect('login')
        try:
            # date
            start_date = first_day_of_the_month_year()
            end_date = today_date()
            # raw queries
            data = sql_connection(start_date, end_date)
            factories = Factory.objects.filter(is_delete=False).values('factory_name')
            items = Item.objects.filter(is_delete=False).values('item_name')
            # print(data)
        except Exception as exe:
            logger.error(str(exe), exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['today_date'] = end_date if end_date else ''
        content['start_date'] = start_date if start_date else ''
        content['factories'] = factories if factories else ''
        content['items'] = items if items else ''
        content['data'] = data if data else ''
        return render(request, self.template_name, content)
    
    def post(self, request):
        if not auth(request):
            return redirect('login')
        
        try:
            data = request.POST
            start_date = data.get('start_date')
            end_date = data.get('end_date')

            data = sql_connection(start_date, end_date)
            factories = Factory.objects.filter(is_delete=False).values('factory_name')
            items = Item.objects.filter(is_delete=False).values('item_name')
        
        except Exception as exe:
            logger.error(str(exe) , exc_info=True)
            
        content = {}
        content['page_title'] = self.page_title
        content['today_date'] = end_date if end_date else ''
        content['start_date'] = start_date if start_date else ''
        content['factories'] = factories if factories else ''
        content['items'] = items if items else ''
        content['data'] = data if data else ''
        return render(request, self.template_name, content)
            


            




