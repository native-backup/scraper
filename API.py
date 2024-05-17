from fastapi import FastAPI
from pydantic import BaseModel
from utils import calc_params
from scraper import Scraper


class DesireParams(BaseModel):
    activity: int
    money: int
    play: int
    knowledge: int
    independence: int


app = FastAPI()


@app.get("/params", response_model=DesireParams)
async def root(
    year: int,
    month: int,
    day: int,
    sex: str,
):
    scraper = Scraper(
        driver_path="chromedriver",
        start_year=1990,
        end_year=2010,
        end_month=1,
        end_day=10,
    )
    params = calc_params(scraper, year, month, day, sex)

    return DesireParams(
        activity=params["行動"],
        money=params["お金"],
        play=params["遊び"],
        knowledge=params["知識"],
        independence=params["自立"],
    )
