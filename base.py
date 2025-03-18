import requests, schedule, time
from bs4 import BeautifulSoup

from twilio.rest import Client

def run_check(url, referer):
    # Headers to mimic a real browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Referer": referer,
        "Accept-Language": "en-US,en;q=0.9",
    }

    # Make request
    response = requests.get(url, headers=headers)

    # Check if request is blocked
    if response.status_code == 403:
        return "Request blocked by" + referer
    else:
        # Parse HTML
        soup = BeautifulSoup(response.content, "html.parser")
        
        if referer == "https://www.bestbuy.com/":
            # Find the "Add to Cart" button
            button = soup.find("button", {"data-button-state": True})
            price_element = soup.find("div", class_="priceView-hero-price priceView-customer-price")
            price = price_element.find("span").text if price_element else "[X.XX]"


            if button and "disabled" in button.attrs:
                stock_status = "Item is NOT AVAILABLE."
            else:
                stock_status = "Item is IN STOCK for " + price + "!"

        elif referer == "https://www.target.com/":
            # Find the Add to Cart button
            button = soup.find('button', class_= "styles_ndsBaseButton__W8Gl7 styles_md__X_r95 styles_mdGap__9J0yq styles_fullWidth__3XX6f styles_ndsButtonPrimary__tqtKH")
            price_element = soup.find("span", {"data-test": "product-price"})
            price = price_element.text.strip() if price_element else "Price not found"

            if button:
                is_disabled = "disabled" in button.attrs
                print(f"✅ Button Found! Disabled: {is_disabled}")
                stock_status = "Item is IN STOCK for " + price + "!"
            else:
                stock_status = "Item is NOT AVAILABLE."

    return stock_status
    


