def receipts_validation(request):
    data = request.POST
    date = data.get('date')
    owner_id = data.get('owner_id')
    account_id = data.get('mode_of_payment')
    amount = data.get('amount')
    error_list = []

    if not date:
        error_list.append('date is null')

    if not owner_id:
        error_list.append('owner is null')
    
    if not account_id:
        error_list.append('mode of payment is not valid')
    
    if not amount:
        error_list.append('opening_balance is null')
    
    return error_list, date, account_id, owner_id, amount