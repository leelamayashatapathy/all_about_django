

import os
import django
import requests

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Fulltextsearch.settings')
django.setup()




# from textsearch.models import Product


# url = 'https://dummyjson.com/products?limit=300'
# response = requests.get(url)
# data = response.json()

# for product_data in data['products']:
#     try:
#         product = Product(
#             title=product_data['title'],
#             description=product_data['description'],
#             category=product_data['category'],
#             price=product_data['price'],
#             brand=product_data.get('brand'),
#             sku=product_data['sku'],
#             thumbnail=product_data['thumbnail']
#         )
#         product.save()
#     except Exception as e:
#         print(e)


