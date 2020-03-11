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
                       "page_size": 30
                       }

        response = requests.get(api, params=payload)
        results = response.json()
        all_products.extend(results['products'])
        return all_products

    def final_response(self,all_products):
        final_selected_product = []

        for product in all_products:
            categories = product['categories']
            name = product['product_name_fr']
            nutrition_grade = product['nutrition_grade_fr']
            url = product['url']
            description = product['generic_name_fr']
            stores = product['stores']
            barcode = product['code']
            key = (barcode, name,nutrition_grade, url,description,stores,categories)
            final_selected_product.append(key)
        return final_selected_product

def main():
    data_collect = Api_data()
    api_connection = data_collect.connect_and_sort()
    data_collect.final_response(api_connection)


if __name__=="__main__":
    main()







