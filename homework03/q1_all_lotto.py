import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook()
ws = wb.active

last_lotto_num = 861

for row in range(last_lotto_num):
    url = "https://search.daum.net/search?w=tot&rtmaxcoll=LOT&DA=LOT&q="+str(row)+"%ED%9A%8C%EC%B0%A8%20%EB%A1%9C%EB%98%90"
    print(url)
    req = requests.get(url)

    if req.status_code != requests.codes.ok:
        exit()

    html = BeautifulSoup(req.text, 'html.parser')
    lotto_numbers = html.select('span.img_lotto')

    for index, number in enumerate(lotto_numbers, start=1):
        ws.cell(row, index, value=int(number.text))
    row += 1

wb.save("lotto_all.xlsx")