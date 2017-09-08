#-*- coding: utf-8 -*-
import url_manager
import html_downloader
import html_parser
import html_outputer

class SpiderMan(object):
     def __init__(self):
         self.urls = url_manager.UrlManager()
         self.downloader = html_downloader.HtmlDownloader()
         self.parser = html_parser.HtmlParser()
         self.outputer = html_outputer.HtmlOutPuter()


     def craw(self, root_url):
         count = 1
         self.urls.add_new_url(root_url)
         while self.urls.has_new_url():
             print 'craw %d item'%count
             new_url = self.urls.get_new_url()
             html_cont = self.downloader.download(new_url)
             new_urls, new_data = self.parser.parse(new_url, html_cont)
             self.urls.add_new_urls(new_urls)
             self.outputer.collect_data(new_data)

             if count == 10:
                 break

             count += 1

         self.outputer.output_html()



if __name__ == "__main__":
    spider = SpiderMan()
    spider.craw("https://baike.baidu.com/item/%E5%91%A8%E6%98%9F%E9%A9%B0")


