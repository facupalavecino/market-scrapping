from pathlib import Path
from classes import CarrefourScrapper
import json

def main():
    """
    Reads a list of market products and scraps the web looking for prices
    """
    products = json.load(open('products.json'))
    carrefour = CarrefourScrapper()

    df = carrefour.analyze(products)

    print(df.transpose())

    # if Path(PRICES_CSV).is_file():
    #     df = pd.DataFrame([row], columns=headers)
    #     df.to_csv(PRICES_CSV, mode='a', index=False, header=False)
    # else:
    #     df = pd.DataFrame([row], columns=headers)
    #     df.to_csv(PRICES_CSV)


if __name__ == '__main__':
    print(f'Searching prices...')
    main()
