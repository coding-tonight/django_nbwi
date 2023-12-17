from django.db import connection

from factory.models import Factory
from group.models import Group


def report_summary():
    """ query for item wise sale report
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(''' 
                            select transactions.date , transactions.amount_received,transactiondetail.group_id from  transactions 
                            inner join transactiondetail on transactiondetail.transaction_id = transactions.id
                            where transactions.is_delete=0;  
                           ''')
            row = cursor.fetchall()

        factories = Group.objects.filter(
            is_delete=False).values('id', 'group_name')
        # print(row)
        # list_date = [ dict(data) for data in row]
        # print(list_date)

        # filter value only for label for the chart
        labels = [factory['group_name'] for factory in factories]

        # converting raw data into list of dict
        keys = ['date', 'amount', 'group_id']
        group_dict_list = [dict(zip(keys, data)) for data in row]
        # print(new_dict)

        group_wise_sale = []
        for factory in factories:
            # inital value for each group
            group_wise = {
                'group_name': factory['group_name'],
                'amount': 0 # inital start with zero 
            }

            for group in group_dict_list:
                # if id match then sum the amount with pervious amount
                if factory['id'] == group['group_id']:
                    group_wise['amount'] += group['amount'] 
            
            group_wise_sale.append(group_wise)

        return labels ,group_wise_sale
    except Exception as exe:
        raise Exception(exe)
