from billing.models import Transaction
from app.messages import globalMessage


def invoiceValidation(request):
    data = request.POST
    error_list = []
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
    total_amount = data.get('total_amount')
    total_recevied = data.get('total_recevied')
    total_product_charge = data.get('total_product_charge')
    total_vehicle_rent = data.get('total_vehicle_rent')
    total_wrapping = data.get('total_wrapping')
    total_label_charge = data.get('total_label_charge')

    # null check
    if not ref_no or not factory_id:
        error_list.append(f'Ref no or factory {globalMessage.NULL_MESSAGE}')

    if not item_id and item_qty and group_id and account_id:
        error_list.append(f'{globalMessage.NULL_MESSAGE}')

    if len(date) == 0:
        error_list.append(f'Date: {globalMessage.NULL_MESSAGE}')

    if Transaction.objects.filter(ref_no=ref_no).exists():
        error_list.append(f'Ref no:{globalMessage.DUPLICATE_ERROR_MESSAGE}')

    return error_list
