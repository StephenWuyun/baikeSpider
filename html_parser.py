#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urlparse
import re


class HtmlParser(object):
    @staticmethod
    def _get_new_urls(page_url, soup):
        new_urls = list()
        #/item/史记·2016?fr=navbar
        links = soup.find_all('a', href=re.compile("/item/."))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            if new_full_url not in new_urls:
                new_urls.append(new_full_url)

        return new_urls

    @staticmethod
    def _get_new_data(page_url, soup):
        res_data = {}
        #url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"> <h1>周星驰<h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        #summary
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

