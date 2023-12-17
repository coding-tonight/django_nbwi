from django.db import connection

def sql_connection(start_date, end_date):
    try:
        # raw queries for item wise sale report
        with connection.cursor() as cursor:
            cursor.execute(f'''select transactions.date , factory.factory_name , salegroup.group_name as groupsale ,transactiondetail.item_qty, item.item_name , item.item_type 
                                from  factory 
                                inner join transactions on factory.id = transactions.factory_id
                                inner join transactiondetail on transactiondetail.transaction_id = transactions.id
                                inner join salegroup on salegroup.id = transactiondetail.group_id
                                inner join item on item.id = transactiondetail.item_id
                                where transactions.date between '{start_date}' and '{end_date}'
                                order by transactions.created_at;
                        ''') 
            # cursor.execute('select * from item')
            row = cursor.fetchall()
            
        #  keys for data of the sale report
        keys = ['bill_date' , 'factory_name' , 'sale_group', 'item_qty', 'item_name' , 'item_type']
        data_list = [ dict(zip(keys, value)) for value in row ]  # converting list of turple raw  to list of dict 

        # date should not be repeated so set is used here  
        list_date = { data['bill_date'] for data in data_list } # set is created to store date
        
        """ fitlering data with date 
            this function return dict with date as a key 
        """
        filter_data = {}
        def map_by_date(data_list):
            for  date in sorted(list(list_date)):  # sorted by date
                filter_list = list()
                for data in data_list:
                    if data['bill_date'] == date:
                        filter_list.append(data)
                        filter_data[str(date)] = filter_list
            
        
        map_by_date(data_list) 
        # print(filter_data)
        return filter_data
    
    except Exception as exe:
        raise Exception(exe)
    


