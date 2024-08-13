from collections import OrderedDict
from django.db import connections

def dict_fetch_all(cursor):
    """Return all rows from a cursor as a dict"""
    columns = [col[0] for col in cursor.description]
    return [
        OrderedDict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    
    
def execute_query(query):
    try:
        with connections['default'].cursor() as cursor:
            cursor.execute(query)
            data = dict_fetch_all(cursor)
            return data
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []