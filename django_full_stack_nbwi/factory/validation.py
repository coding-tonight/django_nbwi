from factory.models import FactoryOwner


def factoryValidation(request):
    try:
        data = request.POST
        error_list = []
        factory_name = data.get('factory_name')
        address = data.get('factory_address')
        phone_number = data.get('phone_number')
        owner_id = data.get('owner_id')
        
    

        if len(factory_name) == 0 or len(address) == 0:
            error_list.append('Field is null')


        return error_list, factory_name, address, phone_number, owner_id 
    except Exception as exe:
        raise Exception(exe)


def ownerValidation(request):
    data = request.POST
    error_list = []
    owner_name = data.get('owner_name')
    address = data.get('address')
    phone_number = data.get('phone_number')
    opening_balance = data.get('opening_balance') if data.get('opening_balance') else 0

    if not owner_name:
        error_list.append('factory is null')

    if not address:
        error_list.append('address is null')

    if not phone_number:
        error_list.append('phone number is null')

    # if FactoryOwner.objects.filter(factory_id=factory_id).exists():
    #     error_list.append('duplicated factory name')

    return error_list, owner_name, address, phone_number , opening_balance
