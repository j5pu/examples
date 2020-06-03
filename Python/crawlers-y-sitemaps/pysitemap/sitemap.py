from importados.pysitemap import pysitemap

"""
Example script
Uses gevent to implement multiprocessing if Gevent installed
To install gevent:
    $ pip install gevent
"""

if __name__ == '__main__':
#    url = 'https://icobench.com'  # url from to crawl
    url = 'https://icorating.com'  # url from to crawl

    logfile = 'errlog.log'  # path to logfile
    oformat = 'txt'  # output format
    outputfile = 'sitemap.txt'  # path to output file
    crawl = pysitemap.Crawler(url=url, logfile=logfile, oformat=oformat, outputfile=outputfile)
    crawl.crawl(pool_size=20, echo=True)