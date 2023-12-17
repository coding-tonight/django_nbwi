import logging
# from django.contrib.auth.decorators import login_required
from django.views import View
# from django.contrib.auth import excempt
from django.shortcuts import render, redirect
from django.http import JsonResponse

from item.models import Item
from factory.models import FactoryOwner, Factory
from app.middleware import auth
from dashboard.connection import report_summary


logger = logging.getLogger('django')

# Create your views here.


class DashboardView(View):
    template_name = 'dashboard.html'
    page_title = 'Dashboard'

    def get(self, request):
        try:
            if not auth(request):
                return redirect('login')

            try:
                inventory_count = Item.objects.count()
                owner_count = FactoryOwner.objects.count()
                factory_count = Factory.objects.count()

            except Exception as exe:
                raise Exception(exe)

            content = {}
            content['page_title'] = self.page_title
            content['owner_count'] = owner_count if owner_count else ''
            content['inventory_count'] = inventory_count if inventory_count else ''
            content['factory_count'] = factory_count if factory_count else ''
            return render(request, self.template_name, content)

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            return redirect('dashboard')


class ChartData(View):
    """api for chart 
    """

    def get(self, request):
        try:
            if not auth(request):
                return JsonResponse({'msg': 'Not auth'}, status=403)

            labels, group_wise_sale = report_summary()

            # print(labels)
            MSG = {
                'label': labels,
                'group_wise_sale': group_wise_sale
            }
            return JsonResponse(MSG, status=200)

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            return JsonResponse({'msg': 'Ops something went wrong'}, status=500)
