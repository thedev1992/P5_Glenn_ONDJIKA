import requests
from constants import *
from pprint import pprint


class Api_data:
    def __init__(self):
        pass

    def connect_and_sort(self):

        all_products = []

        api = 'https://fr.openfoodfacts.org/cgi/search.pl'
        for category in CATEGORIES:
            payload = {"action": "process",
                       "json": 1,
                       "tagtype_0": "categories",
                       "tag_contains_0": "contains",
                       "tag_0": category,
                       "page_size": quantity
                       }

        response = requests.get(api, params=payload)
        results = response.json()
        all_products.extend(results['products'])
        return all_products

    def final_response(self,all_products):
        final_selected_product = []

        keys = ['id', 'product_name_fr',
                'categories', 'url', 'nutrition_grade_fr',
                'stores', 'generic_name_fr']

        for product in all_products:
            categorie = product['categories']
            stores = product['stores']
            barcode = product['code']
            name = product['product_name_fr']
            url = product['url']
            nutrition_grade = product['nutrition_grade_fr']
            description = product['generic_name_fr']
            key = (barcode, stores, name, url, nutrition_grade, categorie, description)
            final_selected_product.append(key)

        return pprint(final_selected_product)

def main():

    data_collect = Api_data()
    api_connection = data_collect.connect_and_sort()
    data_collect.final_response(api_connection)


if __name__=="__main__":
    main()







