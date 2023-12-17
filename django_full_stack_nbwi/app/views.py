import logging
from django.contrib.auth import authenticate ,logout , login
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from app.middleware import auth


logger = logging.getLogger('django')
# Create your views here.

class LoginView(View):
    template_name = 'login.html'
    page_title = 'NBWI'

    def get(self, request):
        content = {}
        content['page_title'] = self.page_title
        if auth(request):
           return redirect('dashboard')
        else:
           return render(request, self.template_name , content)
    
    def post(self, request):
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username=username , password=password)

        if not user:
            messages.error(request, 'invalid username and password')
            return redirect('login')
        
        login(request, user)
        messages.success(request, 'Successfully Login.')    
        return redirect('dashboard')
    


class Logout(View):
    def get(self ,request):
        try:
            logout(request)
            return JsonResponse({'msg': 'Successfully Logout'}, status=200)
        except Exception as exe:
            logger.error(str(exe) , exc_info=True)
            return JsonResponse({'msg': 'logout fail'}, status=400)
            

