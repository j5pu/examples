import aiohttp
import asyncio
import tqdm

class fetch_url:
    def __init__(self, session, url, timeout=10):
        self.session = session
        self.url = url
        self.timeout = timeout

    async def __aenter__(self):
        async with self.session.get(self.url) as response:
            text = await response.text()
            # print("URL: {} - TEXT: {}".format(self.url, len(text)))
            return text

    async def __aexit__(self, exc_type, exc, tb):
        pass

async def parse_url(session, url, timeout=10):
    # get doc from url
    async with fetch_url(session, url, timeout) as doc:
        # print("DOC: {}".format(doc, len(doc)))
        return doc


async def parse_urls():
    tickers = ['CTXS', 'MSFT', 'AAPL', 'GPRO', 'G', 'INTC', 'SYNC', 'SYNA']
    urls = ["https://finance.yahoo.com/quote/{}".format(ticker) for ticker in tickers]

    async with aiohttp.ClientSession() as session:
        tasks = [parse_url(session, url) for url in urls]
        responses = [await f for f in tqdm.tqdm(asyncio.as_completed(tasks), total = len(tasks))]
        #print(responses)


if __name__ == '__main__':

    asyncio.run(parse_urls())