import requests
from config import TOKEN


class Nasa:
    def __init__(self, token):
        self.token = token

    def get_current_data(self):
        current_req = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={self.token}')
        if current_req.status_code == 200:
            return current_req.json()
        return None

    def get_data_by_date(self, date):
        by_date_req = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={self.token}&date={date}')
        if by_date_req.status_code == 200:
            return by_date_req.json()
        return None

if __name__ == '__main__':
    n1 = Nasa(TOKEN)
    print(n1.get_current_data())
    print(n1.get_data_by_date('2026-01-11'))



