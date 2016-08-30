import re
import urllib.parse
from bs4 import BeautifulSoup
from py.autotest import html_downloader


class HtmlParser(object):
    def parse(self, url, html_content):
        if url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        # /view/123.htm
        # links = soup.find_all('a', href=re.compile(r'(?!javascript)'))
        links = soup.find_all('a')
        for link in links:
            new_url = link['href']
            if new_url.find('javascript') == -1:
                new_full_url = urllib.parse.urljoin(url, new_url)
                new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, url, soup):
        res_data = {'url': url}

        # url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        text = soup.getText()
        if text.find('FreeMarker template error') != -1:
            res_data['error'] = 'FreeMarker Error'

        return res_data


    def get_index_theme(self, url, soup):
        pass
