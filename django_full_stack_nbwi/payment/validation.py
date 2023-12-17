from  factory.models import Factory

def paymentValidation(request):
    data = request.POST
    error_list = []
    date = data.get('date')
    owner_id = data.get('owner_id')
    account_id = data.get('account_id')
    amount = data.get('amount')

   
    if len(date) == 0 or  len(owner_id) ==0  or  len(account_id) == 0 or  len(amount) == 0:
        error_list.append('Field can not be null')

    if not Factory.objects.filter(reference_id=owner_id):
        error_list.append('owner field is null.')

    
    return error_list , date , owner_id , account_id , amount
