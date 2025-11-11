import requests
from bs4 import BeautifulSoup

class StockListFetcher:
    def get_sp500_tickers() -> list:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }

        url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find('table', {'id': 'constituents'})
        table_rows = table.find_all('tr')[1:]

        tickers = []

        for row in table_rows:
            ticker = row.find('a', class_='external text').get_text(strip=True)
            tickers.append(ticker)

        return(tickers)

# Test usage
# fetcher = StockListFetcher()
# print(fetcher.get_sp500_tickers())
