import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()
SMTP_SERVER = os.getenv("SMTP_SERVER")
MY_EMAIL = os.getenv("MY_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")

TARGET_PRICE = 96000  # Set your own target price

# Replace with your own product url from amazon
url = "https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5Z3T4M/ref=sr_1_1_sspa?th=1"
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=header)
soup = BeautifulSoup(response.text, "html.parser")

price = (
    soup.find(class_="a-offscreen").getText().strip("₹")
)  # Replace '₹' with '$' if your'e using amazon.com
title = soup.find(id="title").getText().strip()
float_price = float(price.replace(",", ""))


with open("recipents.txt") as rec_file:
    recipents = [line.strip() for line in rec_file if line.strip()]


if float_price < TARGET_PRICE:
    message = f"Sale Sale Sale!\n\n{title} is on sale for {price}"

    with smtplib.SMTP(SMTP_SERVER, 587) as connection:
        connection.starttls()
        result = connection.login(MY_EMAIL, APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=recipents,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n\n{url}".encode("utf-8"),
        )
