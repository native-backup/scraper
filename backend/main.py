from scraper_async import Scraper
import asyncio

if __name__ == "__main__":

    scraper = Scraper(
        driver_path="chromedriver",
        start_year=1980,
        end_year=2020,
        end_month=12,
        end_day=31,
    )
    asyncio.run(scraper.scrape())
