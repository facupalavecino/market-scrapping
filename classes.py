import requests
import bs4
from datetime import date
import pandas as pd

class CarrefourScrapper:
    """ Class that handles the web-scrapping in the Carrefour website """

    def analyze(self, products: list) -> pd.DataFrame:
        """
        Returns a DataFrame containing each product as a column and their prices as rows.
        
        It adds a column at the beginning with the current day
        """

        headers = []
        row = []

        headers.append('Date')
        row.append(date.today().isoformat())

        for product in products:
            headers.append(product['name'])
            price = None
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
            row.append(price)

        return pd.DataFrame([row], columns=headers)