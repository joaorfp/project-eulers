import pandas_market_calendars as mcal
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import *

class Ticker:
    def __init__(self, data=None):
        if data is None:
            tz = mcal.get_calendar('B3').tz.zone
            self.data = pd.Timestamp.now(tz=tz).date()
        else:
            self.data = pd.to_datetime(data).date()

    def next_data_expire(self, data):
        # gets the day 15 of the month
        day_15 = data + relativedelta(day=15)

        # checks if the month is odd, so it will add 1+ in a month (or not)
        if int(data.month) % 2 != 0: 
            data += relativedelta(month=int(data.month) + 1)
        # gets the day 15 of the month
        day_15 = data + relativedelta(day=15)
        weekday = day_15.weekday()
        print(weekday)

        # gets the diff between the weekday given and wednesday
        previous_wednesday = weekday - 2 if weekday >= 2 else weekday + 4
        next_wednesday = 2 - weekday if weekday <= 2 else 9 - weekday

        # checks the diff to determine if the days will be subtracted or added
        if previous_wednesday <= next_wednesday:
            nearest_wednesday = day_15 - timedelta(days=previous_wednesday)
        else:
            nearest_wednesday = day_15 + timedelta(days=next_wednesday)

        return nearest_wednesday


    def nth_ticket_expiration(self, ticker):
            new_data = datetime.now().date()
            # sum the quantity of months by the parameter
            new_data += relativedelta(month=int(new_data.month) + (ticker * 2))
            return new_data


    def next_ticket_expiration(self, ticker=None):
        b3 = mcal.get_calendar('B3')
        if ticker:
            # if the ticker int is provided, it does the math to that specified month of expiration
            nth_ticket = Ticker.nth_ticket_expiration(self, ticker)
            next_ticket_to_expire = Ticker.next_data_expire(self, nth_ticket)

            # gets the days which the b3 window is open
            datas = b3.schedule(start_date=datetime.now().date(), end_date=next_ticket_to_expire)

            # print how many util days the ticker will expire
            print(f'Ticket will expire at {next_ticket_to_expire}. {len(datas)} days until the ticker n{ticker} from now to expire')
            return f'Ticket will expire at {next_ticket_to_expire}. {len(datas)} days until the ticker n{ticker} from now to expire'

        else:
            next_ticket_to_expire = Ticker.next_data_expire(self, self.data)
            # gets the days which the b3 window is open

            datas = b3.schedule(start_date=datetime.now().date(), end_date=next_ticket_to_expire)
            # print how many util days the ticker will expire

            print(f'Ticket will expire at {next_ticket_to_expire}. Util-Days to ticket expiration: {len(datas)}')
            return f'Ticket will expire at {next_ticket_to_expire}. Util-Days to ticket expiration: {len(datas)}'

ticker = Ticker('2023-03-27')
ticker.next_ticket_expiration()

# ticker = Ticker()
# ticker.next_ticket_expiration(1)

