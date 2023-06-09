import json
import requests
from bs4 import BeautifulSoup
from datetime import datetime


def get_today_date():
    """Return today's date in dd.mm.yyyy format."""
    return datetime.today().strftime('%d.%m.%Y')


class ParserCBRF:
    """Parser for the key rates on the Central Bank of Russia website."""

    def __init__(self, start_url):
        self.start_url = start_url
        self.data = []
        self.session = requests.Session()

    def start(self):
        """Start the parsing process."""
        response = self.session.get(self.start_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        self._parse(soup)
        self._serialize_data()

    def _parse(self, soup):
        """Parse the key rates table."""
        table = soup.find('table', {'class': 'data'})
        rows = table.find_all('tr')

        for row in rows[1:]:
            cols = row.find_all('td')

            date_str = cols[0].text.strip()
            rate_str = cols[1].text.strip().replace(',', '.')
            date = datetime.strptime(date_str, '%d.%m.%Y').strftime('%d.%m.%Y')
            rate = float(rate_str)

            self.data.append({'date': date, 'rate': rate})

    def _serialize_data(self):
        """Save the parsed data to a file in JSON format."""
        with open('cb_rate_and_date.json', 'w') as f:
            json.dump(self.data, f)

    @staticmethod
    def deserialize_data():
        """Load the parsed data from a file in JSON format."""
        with open('cb_rate_and_date.json', 'r') as f:
            cb_rates_data = json.load(f)
        return cb_rates_data


if __name__ == "__main__":
    URL = f'https://cbr.ru/hd_base/KeyRate/?UniDbQuery.Posted=True&UniDbQuery.From=17.09.2013&UniDbQuery.To={get_today_date()}'
    parser = ParserCBRF(URL)
    parser.start()
    loaded_data = ParserCBRF.deserialize_data()