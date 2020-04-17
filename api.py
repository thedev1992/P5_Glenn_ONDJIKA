import requests
from constants import *
from pprint import pprint


class Api:
    """
            This class has the responsibility of collecting a certain number
            of products, in selected categories, thus to give a valid
            structure for the insertion in the database
        """
    def __init__(self):
        """ The constructor is not used here """
        pass

    @staticmethod
    def connect_and_sort():
        """ Use the configuration for the connecting interface """

        all_products = []
        # This config for  for connecting API
        api = 'https://fr.openfoodfacts.org/cgi/search.pl'
        for category in CATEGORIES:
            payload = {"action": "process",
                       "json": 1,
                       # Get the result by category
                       "tagtype_0": "categories",
                       "tag_contains_0": "contains",
                       # the tag represents the article search
                       "tag_0": category,
                       # Number of articles per page
                       "page_size": quantity
                       }

        response = requests.get(api, params=payload)
        results = response.json()
        all_products.extend(results['products'])
        return all_products

    @staticmethod
    def final_response(all_products):
        """ Formatted the response just harvest the categories selected """
        final_selected_product = []

        for product in all_products:
            categories = product['categories']
            name = product['product_name_fr']
            nutrition_grade = product['nutrition_grade_fr']
            url = product['url']
            description = product['generic_name_fr']
            stores = product['stores']
            barcode = product['code']
            key = (barcode, name, nutrition_grade, url, description, stores, categories)
            # Respect of the order of the criteria insert in a tuple
            # and simple format in database insert
            final_selected_product.append(key)
        return final_selected_product


def main():
    """ Initialize the data collect """

    data_collect = Api()
    api_connection = data_collect.connect_and_sort()
    data_collect.final_response(api_connection)


if __name__ == "__main__":
    main()







