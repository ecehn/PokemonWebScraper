import requests, schedule, time
from bs4 import BeautifulSoup

from twilio.rest import Client

def check_BB():
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": "https://www.bestbuy.com/",
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Make request
    response = requests.get(bbUrl, headers=headers)

    # Check if request is blocked
    if response.status_code == 403:
        return "Blocked by Best Buy!"
    else:
        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")

        # Find the "Add to Cart" button
        button = soup.find("button", {"data-button-state": True})
        price_element = soup.find("div", class_="priceView-hero-price priceView-customer-price")
        price = price_element.find("span").text if price_element else "[X.XX]"


        if button and "disabled" in button.attrs:
            stock_status = "Item is NOT AVAILABLE."
        else:
            stock_status = "Item is IN STOCK for " + price + "!"

    return stock_status
    

def run_scraper():
    schedule.every(5).seconds.do(check_BB)

    while True:
        schedule.run_pending()
        time.sleep

