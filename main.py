"""
button.btn-disabled
"""
import requests
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse

bestBuySelector = 'button.btn-disabled'
newEggSelector = "i.fa-exclamation-triangle"


links = [
  'https://www.bestbuy.com/site/macbook-air-13-3-laptop-apple-m1-chip-8gb-memory-256gb-ssd-latest-model-gold/6418599.p?skuId=6418599', 
    'https://www.bestbuy.com/site/dyson-v8-animal-cord-free-stick-vacuum-iron/5712666.p?skuId=5712666',
  'https://www.newegg.com/asus-geforce-rtx-3090-rog-strix-rtx3090-o24g-white/p/N82E16814126482?Description=rtx%203090%20gpu&cm_re=rtx_3090%20gpu-_-14-126-482-_-Product', 
  'https://www.newegg.com/purple-dyson-up13-ball-multi-floor-origin/p/0G1-0006-000H2?Item=9SIADVW6HA9896&cm_sp=Homepage_dailydeals-_-P3_9SIADVW6HA9896-_-04192021&quicklink=true', 

]


headers = {"User-Agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"}

while True:
  for link in links:
    parsed_link = urlparse(link)
    company = parsed_link.netloc
    print(company)

    response = requests.get(link, headers = headers)
    page = response.content

    soup = BeautifulSoup(page, 'html.parser')

    if company == "www.bestbuy.com":
      selector = bestBuySelector
  
    if company == "www.newegg.com":
      selector = newEggSelector
    
    soup.select(selector)

    result = soup.select(selector)
    

    if len(result) == 0: 
      print("IN STOCK")
    else:
      print("OUT OF STOCK")

    time.sleep(15)