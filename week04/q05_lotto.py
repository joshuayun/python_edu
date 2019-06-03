import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q=%EB%A1%9C%EB%98%90+%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8"

req = requests.get(url)

if req.status_code != requests.codes.ok:
    exit()

html = BeautifulSoup(req.text, 'html.parser')
lotto_numbers = html.select('span.img_lotto')

from openpyxl import Workbook

wb = Workbook()
ws = wb.active

for index, number in enumerate(lotto_numbers,start=1):
    ws.cell(1, index, value=int(number.text))

wb.save("lotto.xlsx")

#numbers = [int(number.text) for number in lotto_numbers]
#print(numbers)








