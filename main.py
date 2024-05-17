from scraper import Scraper
from utils import calc_params
import asyncio

if __name__ == "__main__":

    scraper = Scraper(
        driver_path="chromedriver",
        start_year=1950,
        end_year=2020,
        end_month=12,
        end_day=31,
    )
    # asyncio.run(scraper.scrape())
    for i in scraper.read_data(limit=10000):
        print(i.day)

    print(calc_params(scraper, 1950, 1, 6, "1"))
