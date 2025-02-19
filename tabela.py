from playwright.sync_api import sync_playwright
import time
import datetime
import pandas as pd
from io import StringIO

# Format the date as YYYY-MM-DD
date_string = datetime.date.today().strftime("%Y-%m-%d")

# Construct the filename
filename = f"stock_{date_string}.csv"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://stooq.pl/q/f/?s=gv.f')

    try:
        page.get_by_role('button', name="Zgadzam się").click()

        time.sleep(10)
    except Exception as e:
        print(e)
        pass

    stock = page.evaluate('''() => {
        return document.getElementById('fth1').outerHTML;
    }''')

    stock_df,  = pd.read_html(StringIO(stock))
    stock_df.to_csv(f'./data/{filename}')

    browser.close()
