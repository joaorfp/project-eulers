from datetime import date
from project.ticker import Ticker
import pandas as pd

def test_init_with_no_data():
    ticker = Ticker()
    assert ticker.data == date.today()


def test_init_with_data():
    date_str = "2022-02-28"
    ticker = Ticker(data=date_str)
    assert str(ticker.data) == date_str


def test_next_expire():
    ticker = Ticker()
    assert ticker.next_expire(1) == pd.Timestamp('2023-02-28 21:00:00+0000', tz='UTC')


def test_ticker_days_until_expire():
    ticker = Ticker()
    assert ticker.ticker_days_until_expire('BVMF') == 1

