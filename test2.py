from playwright.sync_api import sync_playwright
import time
import datetime
import pandas as pd

# Format the date as YYYY-MM-DD
date_string = datetime.date.today().strftime("%Y-%m-%d")

# Construct the filename
filename = f"eurpln_{date_string}.csv"

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto('https://stooq.pl/q/?s=eurpln')

    try:
        page.get_by_role('button', name="Zgadzam się").click()
        time.sleep(5)
    except:
        pass

    df = pd.DataFrame({'time': [], 'rate': []})

    for i in range(30 * 15):
        rate = page.evaluate('''() => {
            const elem = document.getElementById('aq_eurpln#1_c5') ?? 
                document.getElementById('aq_eurpln_c5');

            return elem.textContent;
        }''')

        rate_time = page.evaluate('''
            () => document.getElementById('aq_eurpln_t1').textContent;
        ''')
        row = pd.DataFrame({'time': [rate_time], 'rate': [rate]})
        df = pd.concat([df, row])
        time.sleep(4)

    df.reset_index(inplace=True, drop=True)
    df.to_csv(f'./data/{filename}')

    browser.close()
