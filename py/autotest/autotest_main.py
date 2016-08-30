import http.client
import http.cookiejar
import json
from urllib import request
from py.autotest import url_manager, html_downloader, html_parser


class AutoTest(object):

    def __init__(self, config):
        self.config = config
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()

    def freemarker_check(self):
        cfg = self.config
        deep = cfg['deep']
        count = 1
        self.urls.add_new_url(cfg['root_url'])
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                # self.outputer.collect_data(new_data)
                print('craw %d : %s' % (count, new_url))

                # if count == size:
                #     break
                count += 1
            except BaseException as e:
                print('craw failed on %d result %s' % (count, e))

        self.outputer.output_html()
        pass


def get_urls():
    with open('../../src/autotesturl.txt', 'r', encoding='utf-8') as file:
        return file.readlines()


def get_url_content(url):
    if not url:
        return None
    if not url.startswith('http://'):
        url += 'http://'
    response = request.urlopen(url)

    if response.getcode() != 200:
        return None

    try:
        read = response.read().decode('utf-8')
    except http.client.IncompleteRead as icread:
        read = icread.partial.decode('utf-8')

    return read


def check_freemarker_error(url, content):
    url = url.replace('\n', '')
    if content.find('FreeMarker template error') != -1:
        print('发现freeMark异常, 链接是%s' % url)
    else:
        print('%s正常' % url)


# def

#
# for u in get_urls():
#     check_freemarker_error(u, get_url_content(u))

if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as jsonFile:
        data = json.loads(jsonFile.read())
        root_url = data['url']
        spiderDeep = data['deep']
        at = AutoTest(data)
        at.run()

input('')
