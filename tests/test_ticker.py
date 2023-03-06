from datetime import datetime, date
from project.ticker import Ticker
import pandas as pd
import unittest
import pandas_market_calendars as mcal
import pandas as pd

class Tests(unittest.TestCase):
    def setUp(self):
        self.date = date.today()

    def test_next_data_expire(self):
        ticker = Ticker()
        assert 1 == 1
        mock_date = datetime.strptime('2023-04-12', '%Y-%m-%d').date()
        assert ticker.next_data_expire(self.date) == mock_date

    def test_nth_ticket_expiration(self):
        ticker = Ticker()
        mock_date = datetime.strptime('2023-06-14', '%Y-%m-%d').date()
        date_nth_ticker = ticker.nth_ticket_expiration(1)
        assert ticker.next_data_expire(date_nth_ticker) == mock_date

        mock_date2 = datetime.strptime('2023-08-16', '%Y-%m-%d').date()
        date_nth_ticker = ticker.nth_ticket_expiration(2)
        assert ticker.next_data_expire(date_nth_ticker) == mock_date2

    def test_next_ticket_expiration(self):
        b3 = mcal.get_calendar('B3')
        param = 1
        ticker = Ticker()
        next_ticket_to_expire = ticker.next_data_expire(self.date)
        datas = b3.schedule(start_date=datetime.now().date(), end_date=next_ticket_to_expire)
        assert ticker.next_ticket_expiration() == f'Ticket will expire at {next_ticket_to_expire}. Util-Days to ticket expiration: {len(datas)}'

        """Test nth ticket"""
        date_nth_ticker = ticker.nth_ticket_expiration(param)
        next_ticket_to_expire = ticker.next_data_expire(date_nth_ticker)
        datas = b3.schedule(start_date=datetime.now().date(), end_date=next_ticket_to_expire)
        assert ticker.next_ticket_expiration(param) == f'Ticket will expire at {next_ticket_to_expire}. {len(datas)} days until the ticker n{param} from now to expire'