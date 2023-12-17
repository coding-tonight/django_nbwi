def rateValidation(request):
    data = request.POST
    error_list = []
    group_id = data.get('group_id')
    item_id = data.get('item_id')
    #  if given  decimal field is null then asign zero as a value
    sale_rate = data.get('sale_rate') if data.get('sale_rate') else 0
    vehicle_rent = data.get('vehicle_rent') if data.get('vehicle_rent') else 0
    product_charge = data.get('product_charge') if data.get(
        'product_charge') else 0
    wrapping = data.get('wrapping') if data.get('wrapping') else 0
    label_charge = data.get('label_charge') if data.get('label_charge') else 0

    if len(group_id) == 0 or len(item_id) == 0 or len(sale_rate) == 0 or len(product_charge) == 0:
        error_list.append('Field is null')

    return error_list, group_id, item_id, sale_rate, product_charge, wrapping, vehicle_rent, label_charge
