# https://stackoverflow.com/questions/46056513/web-scraping-with-python-in-combination-with-asyncio
import requests
from lxml import html
import asyncio

link = "http://quotes.toscrape.com/"

async def quotes_scraper(base_link):
        response = requests.get(base_link)
        tree = html.fromstring(response.text)
        for titles in tree.cssselect("span.tag-item a.tag"):
            await processing_docs(base_link + titles.attrib['href'])

async def processing_docs(base_link):
        response = requests.get(base_link).text
        root = html.fromstring(response)
        for soups in root.cssselect("div.quote"):
            quote = soups.cssselect("span.text")[0].text
            author = soups.cssselect("small.author")[0].text
            print(quote, author)


        next_page = root.cssselect("li.next a")[0].attrib['href'] if root.cssselect("li.next a") else ""
        if next_page:
            page_link = link + next_page
            await processing_docs(page_link)

loop = asyncio.get_event_loop()
loop.run_until_complete(quotes_scraper(link))
loop.close()