from itertools import product
from math import exp


def itemValidation(request):
    try:
        data = request.POST
        error_list = []
        item_name = data.get('item_name')
        item_code = data.get('item_code')
        item_unit = data.get('item_unit')
        item_qty = data.get('item_qty')
        item_type = data.get('item_type')
        item_opening = data.get('item_opening') if data.get('item_opening') else 0
        item_purchase_rate = data.get('item_purchase_rate') if data.get('item_purchase_rate') else 0

        if not item_name:
            error_list.append("name should not be empty")

        if not item_unit:
            error_list.append('item  unit should not be empty')

        return error_list, item_name, item_code, item_qty,  item_unit, item_code, item_opening, item_purchase_rate, item_type

    except Exception as exe:
        raise Exception(exe)
