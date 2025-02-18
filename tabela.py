from playwright.sync_api import sync_playwright
import time
import datetime

# Format the date as YYYY-MM-DD
date_string = datetime.date.today().strftime("%Y-%m-%d")

# Construct the filename
filename = f"eurpln_{date_string}.csv"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://stooq.pl/q/?s=eurpln')

    try:
        page.locator('.fc-primary-button').click()

        time.sleep(5)
    except:
        pass

    rate = page.evaluate('''() => {
        return document.getElementById('aq_eurpln#1_c5').textContent;
    }''')

    with open(f"./data/{filename}", "w") as file:
        file.write(rate)

    browser.close()
