import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def __init__(self, root_url=''):
        self.root_url = root_url

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
        links = filter(self.cross_domain_filter, soup.find_all('a', href=re.compile(r'.*?/.*')))
        for link in links:
            new_url = link['href']
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
            print('发现freeMark异常, 链接是%s' % url)
        return res_data

    def cross_domain_filter(self, link):
        href = link['href']
        return href.find('http') == -1 or href.find(self.root_url) != -1

    @staticmethod
    def resource_parse(url, html_content):
        if html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        js = map(lambda j: urllib.parse.urljoin(url, j['src']),
                 [j for j in soup.find_all('script', src=re.compile(r'.+'))])
        css = map(lambda c: urllib.parse.urljoin(url, c['href']),
                  [c for c in soup.find_all('link', rel=re.compile(r'.+'))])
        return js, css

