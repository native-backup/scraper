from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, FLOAT
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import aiosqlite

Base = declarative_base()


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    minute = Column(Integer)
    sex = Column(String)
    html_string = Column(String)


class Scraper:
    def __init__(
        self,
        driver_path: str,
        start_year: int,
        end_year: int,
        end_month: int,
        end_day: int,
    ):

        self.driver_path = driver_path
        self.dates = self.generate_dates(start_year, end_year, end_month, end_day)
        self.engine = create_engine(f"sqlite:///backend/database.db", echo=False)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    @staticmethod
    def generate_dates(start_year, end_year, end_month, end_day) -> list[datetime]:
        start_date = datetime(start_year, 1, 1)
        end_date = datetime(end_year, end_month, end_day)
        current_date = start_date
        dates = []
        while current_date <= end_date:
            dates.append(current_date)
            current_date += timedelta(days=1)
        return dates

    @staticmethod
    async def request(driver_path, year, month, day, hour, minute, sex) -> str:
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        service = Service()

        with webdriver.Chrome(service=service, options=chrome_options) as driver:
            driver.get("http://aisare-fourpillars.info/index.php")
            driver.find_element(By.NAME, "dat_year").send_keys(str(year))
            driver.execute_script(
                f"document.getElementsByName('dat_month')[0].value = '{month}';"
            )
            driver.execute_script(
                f"document.getElementsByName('dat_day')[0].value = '{day}';"
            )
            driver.find_element(By.NAME, "dat_hour").send_keys(str(0))
            driver.find_element(By.NAME, "dat_minute").send_keys(str(0))
            gen = driver.find_element(By.ID, f"sex0" + sex)
            driver.execute_script("arguments[0].click();", gen)

            kantei_btn = driver.find_element(By.XPATH, "//a[@onclick='kantei();']")
            driver.execute_script("arguments[0].click();", kantei_btn)

            wait = WebDriverWait(driver, 0)
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            html_source = driver.page_source
        return html_source

    async def extract(
        self,
        driver_path: str,
        year: int,
        month: int,
        day: int,
        hour: int,
        minute: int,
        sex: str,
    ) -> str:
        # await asyncio.sleep(1)
        soup = BeautifulSoup(
            await self.request(driver_path, year, month, day, hour, minute, sex),
            "html.parser",
        )
        txt = soup.prettify()
        # with open(f"html_data/output_{year}_{month}_{day}_{hour}.txt", "w") as file:
        #     file.write(txt)
        return txt

    # async def scrape(self) -> None:
    #     with self.Session() as session:
    #         for i in self.dates:
    #             print(i.year, i.month, i.day)
    #             exists = (
    #                 session.query(Data)
    #                 .filter_by(year=i.year, month=i.month, day=i.day)
    #                 .first()
    #             )
    #             if exists:
    #                 continue
    #             res = await self.extract(
    #                 "./chromedriver", i.year, i.month, i.day, 0, 0, "1"
    #             )
    #             data = Data(
    #                 year=i.year,
    #                 month=i.month,
    #                 day=i.day,
    #                 hour=0,
    #                 minute=0,
    #                 sex="1",
    #                 html_string=res,
    #             )
    #             session.add(data)
    #             res = await self.extract(
    #                 "./chromedriver", i.year, i.month, i.day, 0, 0, "2"
    #             )
    #             data = Data(
    #                 year=i.year,
    #                 month=i.month,
    #                 day=i.day,
    #                 hour=0,
    #                 minute=0,
    #                 sex="2",
    #                 html_string=res,
    #             )
    #             session.add(data)
    #             session.commit()
    import aiosqlite

    async def scrape(self) -> None:
        async with aiosqlite.connect("backend/database.db") as db:  # データベース接続
            async with db.execute(
                "SELECT 1"
            ) as cursor:  # テストクエリ（必要に応じて変更）
                await cursor.fetchall()

            for i in self.dates:
                print(i.year, i.month, i.day)

                # データ存在チェックのクエリを非同期で実行
                async with db.execute(
                    "SELECT * FROM Data WHERE year = ? AND month = ? AND day = ?",
                    (i.year, i.month, i.day),
                ) as cursor:
                    exists = await cursor.fetchone()

                if exists:
                    continue

                # 非同期抽出処理（仮定）
                res = await self.extract(
                    "./chromedriver", i.year, i.month, i.day, 0, 0, "1"
                )

                # データ挿入を非同期で実行
                await db.execute(
                    "INSERT INTO Data (year, month, day, hour, minute, sex, html_string) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (i.year, i.month, i.day, 0, 0, "1", res),
                )

                # 別の性別で再抽出と挿入
                res = await self.extract(
                    "./chromedriver", i.year, i.month, i.day, 0, 0, "2"
                )
                await db.execute(
                    "INSERT INTO Data (year, month, day, hour, minute, sex, html_string) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (i.year, i.month, i.day, 0, 0, "2", res),
                )

                await db.commit()  # 変更をコミット

    def read_data(
        self,
        year: int = 1990,
        month: int = 1,
        day: int = 1,
        sex: str = "1",
        limit: int = 1000,
    ) -> list[Data]:
        with self.Session() as session:
            data = (
                session.query(Data)
                .filter_by(year=year, month=month, day=day, sex=sex)
                .limit(limit)
                .all()
            )
        return data
