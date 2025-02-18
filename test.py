import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://stooq.pl/q/?s=eurpln')

    await page.click('.fc-primary-button')

    await asyncio.sleep(5)

    rate = await page.evaluate('''() => {
        return document.getElementById('aq_eurpln#1_c5').textContent;
    }''')

    print(rate)
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())
