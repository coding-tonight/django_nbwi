import logging
from datetime import datetime

from django.views import View
from django.db import transaction, IntegrityError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages

from group.models import Group
from group.validation import groupValidation
from app.messages import globalMessage
from app.middleware import auth

# Create your views here.
logger = logging.getLogger('django')

class GroupView(View):
    template_name = 'grouptable.html'
    page_title = 'Group'
    """ group views access if only the user is authenticated retirve all the group list data
    """
    def get(self, request):
        if not auth(request):  # check if user is authenticated or not
            return redirect('login')
        
        try:
            groups = Group.objects.filter(is_delete=False)
        except Group.DoesNotExist as exe:
            logger.error(exe)
            groups = ''

        content = {}
        content['page_title'] = self.page_title
        content['groups'] = groups if groups else ''
        return render(request, self.template_name, content)


class GroupAdd(View):
    template_name = 'groupadd.html'
    page_title = 'Add Group'

    def get(self, request):
        if not auth(request):
            return redirect('login')
        
        content = {}
        content['page_title'] = self.page_title
        return render(request, self.template_name, content)

    def post(self,  request):
        try:
            if not auth(request): # check if user is login or not
                return redirect('login')
            
            error_list, group_name = groupValidation(request)
            if error_list:
                messages.error(request, error_list[0])
                return redirect('addGroup')
            
            try:
                with transaction.atomic():
                    sid = transaction.savepoint() # creating sid 

                    Group.objects.create(group_name=group_name, created_at=datetime.now())
                    messages.success(request, globalMessage.SUCCESS_MSG)
                    #  if group is created then transaction savepoint commit 
                    transaction.savepoint_commit(sid) 
                    return redirect('group')
            
            except IntegrityError as exe:
                #  if there is intergrity error then rollback
                transaction.savepoint_rollback(sid)
                raise Exception(exe)
        
        except Group.DoesNotExist as exe:
            logger.error(str(exe) , exc_info=True)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('group')
            


class GroupDetail(View):
    template_name = 'groupedit.html'
    page_title = 'Edit Group'

    def get(self, request, ref_id):
        try:
            if not auth(request):  # check if user is login or not 
                return redirect('login')
            
            group = Group.objects.get(reference_id=ref_id)
            content = {}
            content['page_title'] = self.page_title
            content['group'] = group
            return render(request, self.template_name, content)

        except Group.DoesNotExist as exe:
            logger.error(exe)
            return redirect('group')

    def post(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')
            
            error_list, group_name = groupValidation(request)

            if error_list:
                messages.error(request, error_list[0])
                return redirect('editGroup')
            
            group = Group.objects.get(reference_id=ref_id)
            group.group_name = group_name
            group.updated_at = datetime.now()
            group.updated_by = request.user
            group.save()

            messages.success(request, globalMessage.SUCCESS_MSG)
            return redirect('group')
        
        except Group.DoesNotExist as exe:
            logger.error(exe)
            messages.error(request, globalMessage.ERROR_MSG)
            return redirect('group')


class GroupDelete(View):
    def delete(self, request, ref_id):
        try:
            if not auth(request):
                return redirect('login')
            
            Group.objects.filter(reference_id=ref_id).update(is_delete=True)
            messages.success(request, 'Group successfully deleted.')
            return JsonResponse({"message": " Successfully deleted!"})
        except Group.DoesNotExist as exe:
            logging.error(exe)
            return JsonResponse({"message": "Task Fail"})
