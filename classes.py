import requests
import bs4
from datetime import date
import pandas as pd


class CarrefourScrapper:
    """ Class that handles the web-scrapping in the Carrefour website """

    def analyze(self, products: list) -> pd.DataFrame:
        headers = [['Name', 'Category', 'Price'], [None, None, None]]
        rows = []

        for product in products:
            name = product['name']
            category = product['category']
            price = None
            print(f'Searching price of {name}')
            req = requests.get(product['url'])
            if req.status_code == 200:
                soup = bs4.BeautifulSoup(req.content, 'html.parser')

                element = soup.find(id=product['element_id'])

                if element is not None:
                    price = float(element.text
                                  .replace('\n', '')
                                  .replace(' ', '')
                                  .replace('$', '')
                                  .replace(',', '.'))
            rows.append([name, category, price])
            headers[1][2] = date.today().isoformat()

        return pd.DataFrame(rows, columns=headers)
