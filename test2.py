from playwright.sync_api import sync_playwright
import time

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

    print(rate)

    browser.close()
