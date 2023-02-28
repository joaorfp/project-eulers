import pandas_market_calendars as mcal
import pandas as pd

class Ticker:
    def __init__(self, data=None):
        if data is None:
            tz = mcal.get_calendar('BVMF').tz.zone
            self.data = pd.Timestamp.now(tz=tz).date()
        else:
            self.data = pd.to_datetime(data).date()
        
    def next_expire(self, n=1):
        calendar = mcal.get_calendar('BVMF')
        schedule = calendar.schedule(start_date=self.data, end_date=self.data + pd.DateOffset(years=1))
        expirations = schedule['market_close'].sort_values()
        print(type(expirations.iloc[n-1]))
        return expirations.iloc[n-1]
    
    def days_until_expire(self, n=1):
        expire = self.next_expire(n)
        calendar = mcal.get_calendar('BVMF')
        schedule = calendar.schedule(start_date=self.data, end_date=expire)
        util_days = len(schedule)
        print(util_days)
    
    def ticker_days_until_expire(self, ticker):
        calendar = mcal.get_calendar(ticker)
        schedule = calendar.schedule(start_date=self.data, end_date=self.next_expire())
        util_days = len(schedule)
        return util_days

ticker = Ticker()
exp = ticker.next_expire(10)
print(exp)