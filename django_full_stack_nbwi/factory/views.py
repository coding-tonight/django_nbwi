import logging
from datetime import datetime

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from factory.validation import factoryValidation, ownerValidation
from factory.models import Factory, FactoryOwner
from app.messages import globalMessage
from app.middleware import auth

# Create your views here.

logger = logging.getLogger('django')


class FactoryView(View):
    template_name = 'factorytable.html'
    page_title = 'Factory'

    def get(self, request):
        if not auth(request):
            return redirect('login')

        try:
            factories = Factory.objects.filter(is_delete=False)
        except Factory.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['factories'] = factories if factories else ''
        return render(request, self.template_name, content)


class FactoryAdd(View):
    template_name = 'addfactory.html'
    page_title = 'Add Factory'

    def get(self, request):
        if not auth(request):
            return redirect('login')

        try:
            owners = FactoryOwner.objects.filter(is_delete=False)
        except FactoryOwner.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['owners'] = owners if owners else ''
        return render(request, self.template_name, content)

    def post(self, request):
        try:
            if not auth(request):
                return redirect('login')

            error_list, factory_name, address, phone_number, owner_id = factoryValidation(
                request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('addFactory')

            owner = FactoryOwner.objects.get(pk=owner_id)
            Factory.objects.create(factory_name=factory_name, owner_id=owner,
                                   factory_address=address, phone_number=phone_number, created_at=datetime.now())
            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('factory')

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('factory')


class FactoryDetail(View):
    template_name = 'editfactory.html'
    page_title = 'Edit Factory'

    def get(self, request, ref_id):
        if not auth(request):
            return redirect('login')

        try:
            factory = Factory.objects.get(reference_id=ref_id)
            owners = FactoryOwner.objects.filter(is_delete=False)
        except Factory.DoesNotExist as exe:
            logging.error(exe)

        content = {}
        content['page_title'] = self.page_title
        content['factory'] = factory if factory else ''
        content['owners'] = owners if owners else ''
        return render(request, self.template_name, content)

    def post(self, request, ref_id):
        if not auth:
            return redirect('login')

        try:
            error_list, factory_name, factory_address, phone_number, owner_id = factoryValidation(
                request)

            if error_list:
                messages.error(request, 'Field can be null')
                return redirect('editFactory')

            owner = FactoryOwner.objects.get(pk=owner_id)
            Factory.objects.filter(reference_id=ref_id).select_for_update().update(factory_name=factory_name, factory_address=factory_address, owner_id=owner,
                                                                                   phone_number=phone_number, created_at=datetime.now(), created_by=request.user)

            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('factory')

        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, 'ops something went wrong.')
            return redirect('editFactory')


class OwnerView(View):
    template_name = 'ownertable.html'
    page_title = 'Owner'

    def get(self, request):
        if not auth(request):
            return redirect('login')

        try:
            factory_owners = FactoryOwner.objects.filter(is_delete=False)
        except FactoryOwner.DoesNotExist as exe:
            logger.error(str(exe), exc_info=True)

        content = {}
        content['page_title'] = self.page_title
        content['factoryOwners'] = factory_owners if factory_owners else ''
        return render(request, self.template_name, content)


class OwnerAdd(View):
    template_name = 'addowner.html'
    page_title = 'Add Owner'

    def get(self, request):
        if not auth(request):
            return redirect('login')

        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)

    def post(self,  request):
        try:
            if not auth(request):
                return redirect('login')
            
            error_list, owner_name, address, phone_number, opening_balance = ownerValidation(
                request)

            if error_list:
                messages.error(request, 'field  can not be null')
                return redirect('addOwner')
            
            FactoryOwner.objects.create(owner_name=owner_name, address=address, opening_balance=opening_balance,
                                        phone_number=phone_number, created_at=datetime.now())
            messages.success(request, globalMessage.SUCCESS_MSG)

            return redirect('owner')
        
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('owner')


class OwnerDetail(View):
    template_name = 'editowner.html'
    page_title = 'Edit Owner'

    def get(self, request, pk):
        if not auth(request):
            return redirect('login')

        try:
            owner = FactoryOwner.objects.get(pk=pk)

        except FactoryOwner.DoesNotExist as exe:
            logging.error(exe)

        content = {}
        content['page_title'] = self.page_title
        content['owner'] = owner if owner else ''
        return render(request, self.template_name, content)

    def post(self, request, pk):
        try:
            if not auth(request):
                return redirect('login')

            error_list, owner_name, address, phone_number, opening_balance = ownerValidation(
                request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('owner')

            FactoryOwner.objects.filter(pk=pk).update(owner_name=owner_name, address=address, opening_balance=opening_balance,
                                                    phone_number=phone_number, created_at=datetime.now())
            return redirect('owner')
        
        except Exception as exe:
            logger.error(str(exe), exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('owner')
