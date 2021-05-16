import smtplib
from bs4 import BeautifulSoup
import requests

USER = "iamgrace2113@gmail.com"
PASSWORD = "YOUR_PASSWORD"
AMAZON_SEARCH_ENDPOINT = "https://www.amazon.in/Samsung-Galaxy-Watch-Active-SM-R820NZKAINU/dp/B07ZD69171/ref=sr_1_1_" \
                         "sspa?crid=O4SCYT5WCGIA&dchild=1&keywords=samsung%2Bactive%2Bwatch%2B2&qid=1619819766&spref" \
                         "ix=samsung%2Bactiv%2Caps%2C355&sr=8-1-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyN0ZWUVlVNlUyTz" \
                         "Y3JmVuY3J5cHRlZElkPUEwMDc3NjQ3M1FLTzg4MTBMMzY4RiZlbmNyeXB0ZWRBZElkPUEwNjU5MDgxMUhINzM4WThF" \
                         "M0ZDNCZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU&th=1"
headers = {
    "Accept-Language": "en-US,en;q=0.9,ta;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430."
                  "93 Safari/537.36",
}

response = requests.get(url=AMAZON_SEARCH_ENDPOINT, headers=headers)
active_2_webpage = response.text

soup = BeautifulSoup(active_2_webpage, "html.parser")
price = soup.find(name="span", id="priceblock_ourprice").getText()
print(price)
product_title = soup.find(name="span", id="productTitle").getText().strip()

price_str = ""
for p in price.split()[1].split(','):
    price_str += p
price_of_watch = float(price_str)

if price_of_watch < 20000.00:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=USER, password=PASSWORD)
    connection.sendmail(from_addr=USER, to_addrs="jasigraceit9@gmail.com", msg=f"Subject: Amazon Price ALert!\n\n{product_title} is {price_of_watch}.\n{AMAZON_SEARCH_ENDPOINT}")
    connection.close()
