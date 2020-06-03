import time

from config import log
from lxml import html
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException, WebDriverException
from selenium.webdriver.common.proxy import Proxy, ProxyType


class Browser:
    def __init__(self, url, click_text='', click_times=0, click_delay=3, scroll_times=0, scroll_delay=3):
        self.url = url
        self.click_text = click_text
        self.click_times = click_times
        self.click_delay = click_delay
        self.scroll_times = scroll_times
        self.scroll_delay = scroll_delay
        self.error = False
        self.error_message = ''
        self.proxy = Proxy()
        self.proxy.proxy_type = ProxyType.MANUAL
        self.proxy.http_proxy = '127.0.0.1:9950'
        self.capabilities = webdriver.DesiredCapabilities.FIREFOX
        self.proxy.add_to_capabilities(self.capabilities)
        self.firefox = webdriver.Firefox(desired_capabilities=self.capabilities)
        self.firefox.implicitly_wait(30)

    def download(self):
        if self.open():
            if self.click() is False:
                self.quit()
                return False
        else:
            self.quit()
            return False
        return self.scroll()

    def click(self):
        l = log()
        if self.click_times != 0:
            for i in range(1, self.click_times):
                try:
                    self.firefox.find_element_by_link_text(self.click_text).click()
                    message = 'Click: {} out of {} times - url={}'.\
                        format(i, self.click_times - 1, self.url)
                    l.info(message)
                except NoSuchElementException and NoSuchWindowException as exception:
                    if self.url == "https://icorating.com/ico/all/" and i >= 161:
                        return True
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'. \
                        format(i, self.click_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Click error: {} out of {} times - url={} - Exception: {}'.\
                        format(i, self.click_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.click_delay)
        return True

    def scroll(self):
        l = log()

        if self.scroll_times != 0:
            for i in range(1, self.scroll_times):
                # Nota: hacer un try?
                try:
                    self.firefox.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    message = 'Scroll: {} out of {} times - url={}'.\
                        format(i, self.scroll_times - 1, self.url)
                    l.info(message)
                except WebDriverException as exception:
                    self.error = True
                    self.error_message = 'Scrolling error time={} out of {} times with url={} - Exception: {}'.\
                        format(i, self.scroll_times - 1, self.url, repr(exception))
                    l.error(self.error_message)
                    self.quit()
                    return False
                finally:
                    time.sleep(self.scroll_delay)
        page_source = self.firefox.page_source
        self.quit()
        return page_source

    def open(self):
        l = log()

        try:
            self.firefox.get(self.url)
        except WebDriverException as exception:
            self.error = True
            self.error_message = 'Error opening url={} - Exception: {}'.format(self.url, repr(exception))
            l.error(self.error_message)
        finally:
            tree = html.fromstring(self.firefox.page_source)
            title = tree.xpath('/html/head/title/text()')
            try:
                if title[0] == 'Server Not Found':
                    error = tree.xpath('// *[ @ id = "errorShortDescText"]/text()')

                    self.error = True
                    self.error_message = '{0} - {2} - url={1}'.format(title[0], self.url, error[0])
                    l.error(self.error_message)
            except IndexError as exception:
                self.error = True
                self.error_message = 'Invalid url={} - Exception: {}'.format(self.url, repr(exception))
                l.error(self.error_message)
            if self.error:
                self.quit()
                return False
            else:
                return True

    def close(self):
        self.firefox.close()

    def quit(self):
        self.firefox.quit()


def browser():
    l = log()

    crawl_url = "https://tgram.io/topic/29/it/cryptocurrency"
    page = Browser(url=crawl_url, scroll_times=12)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'cryptocurrency.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://tgram.io/topic/51/it/crypto-mining"
    page = Browser(url=crawl_url, scroll_times=2)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'crypto-mining.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

    crawl_url = "https://icorating.com/ico/all/"
    page = Browser(url=crawl_url, click_text='Show more', click_times=180)
    page_source = page.download()
    if page_source is False:
        l.e(msg='Error downloading page source for url: {}'.format(crawl_url))
    else:
        l.i(msg='Success: source code for url: {}'.format(crawl_url))
        file = 'corating.html'
        try:
            with open(file, 'w') as f:
                f.write(format(page_source))
            l.i(msg='Success: source code for url: {} - saved to {}'.format(crawl_url, file))
        except:
            l.i(msg='Error: source code for url: {} - not saved to {}'.format(crawl_url, file))

browser()