from urllib import parse
import json
# from py.autotest import url_manager, html_downloader, html_parser, html_outputer
# noinspection PyUnresolvedReferences
import url_manager, html_downloader, html_parser, html_outputer


class AutoTest(object):

    def __init__(self, config):
        self.config = config
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser(root_url=config['url'])
        self.outputer = html_outputer.HtmlOutputer()

    def freemarker_check(self):
        cfg = self.config
        self.urls.add_new_url(cfg['url'])
        deep = cfg['deep']
        self.urls.add_new_url(cfg['url'])
        for i in range(0, deep):
            temp_set = set()
            while self.urls.has_new_url():
                u = self.urls.get_new_url()
                collected = False
                try:
                    print(u)
                    html_content = self.downloader.download(u)
                    new_urls, new_data = self.parser.parse(u, html_content)
                    temp_set |= new_urls
                    self.outputer.collect_data(new_data)
                    collected = True
                except BaseException as e:
                    print('craw %s failed, result %s ' % (u, e))
                    if not collected:
                        self.outputer.collect_data({'url': u, 'error': e})
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
            new_data = {'url': j}
            if self.downloader.ping_success(j):
                print(j)
            else:
                print('%s can\'t load' % j)
                new_data['error'] = 'JS failed load'

            self.outputer.collect_data(new_data)

        for c in css:
            new_data = {'url': c}
            if self.downloader.ping_success(c):
                print(c)
            else:
                print('%s can\'t load' % c)
                new_data['error'] = 'CSS failed load'
            self.outputer.collect_data(new_data)
        print('js & css check over')

    def login(self):
        self.downloader.login({
            'username': self.config['id'],
            'password': self.config['pw']
        }, parse.urljoin(self.config['url'], self.config['login_url']))


if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as jsonFile:
        data = json.loads(jsonFile.read())
        at = AutoTest(data)
        at.login()
        at.freemarker_check()
        at.resources_check()
        at.outputer.output_html()
