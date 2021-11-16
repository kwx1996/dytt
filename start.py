from scrapy.utils.reactor import install_reactor
from twisted.internet import reactor, defer, asyncioreactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
import time
import logging
from scrapy.utils.project import get_project_settings

from dytt.spiders.dy_tt import DyTtSpider

configure_logging()
# asyncioreactor.install(asyncio.get_event_loop())
install_reactor('twisted.internet.asyncioreactor.AsyncioSelectorReactor')
runner = CrawlerRunner(get_project_settings())


@defer.inlineCallbacks
def crawl():
    times = 1
    while times > 0:
        logging.info("new cycle starting")
        yield runner.crawl(DyTtSpider)
        times -= 1
    reactor.stop()


crawl()
reactor.run()
