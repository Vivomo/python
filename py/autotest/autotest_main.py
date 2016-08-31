import http.client
import http.cookiejar
import re
from urllib import request, parse
import json
from urllib.request import urlopen, Request
from py.autotest import url_manager, html_downloader, html_parser


class AutoTest(object):

    def __init__(self, config):
        self.config = config
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser(root_url=config['url'])

    def freemarker_check(self):
        cfg = self.config
        self.urls.add_new_url(cfg['url'])
        deep = cfg['deep']
        self.urls.add_new_url(cfg['url'])
        for i in range(0, deep):
            temp_set = set()
            while self.urls.has_new_url():
                u = self.urls.get_new_url()
                try:
                    html_content = self.downloader.download(u)
                    new_urls, new_data = self.parser.parse(u, html_content)
                    temp_set |= new_urls
                    print(u)
                except BaseException as e:
                    print('craw %s failed, result %s ' % (u, e))
            self.urls.add_new_urls(temp_set)

        # self.outputer.output_html()
        print('FreeMarker error check over')

    def resources_check(self):
        """
        check js & css of root_url
        :return:
        """
        html_content = self.downloader.download(self.config['url'])
        js, css = self.parser.resource_parse(self.config['url'], html_content)
        for j in js:
            if self.downloader.ping_success(j):
                print(j)
            else:
                print('%s can\'t load' % j)

        for c in css:
            if self.downloader.ping_success(c):
                print(c)
            else:
                print('%s can\'t load' % c)
        print('js & css check over')

    def login(self):
        _data = {
            'username': self.config['id'],
            'password': self.config['pw']
        }
        post_data = parse.urlencode(_data).encode()
        resp = request.urlopen(parse.urljoin(self.config['url'], self.config['login_url']), data=post_data)
        cookie = []
        headers = resp.headers._headers
        for k, v in headers:
            if k == 'Set-Cookie':
                cookie.append(re.search(r'\w+=.+?;', v).group())
        self.downloader.cookie_str = ' '.join(cookie)

if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as jsonFile:
        data = json.loads(jsonFile.read())
        at = AutoTest(data)
        # at.login()
        # at.freemarker_check()
        at.resources_check()

input('')
