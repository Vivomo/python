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
        self.urls.add_new_url(cfg['url'])
        temp = {cfg['url']}
        deep = cfg['deep']
        r = range(0, deep)
        for i in r:
            temp_set = set()
            for u in temp:
                try:
                    html_content = self.downloader.download(u)
                    new_urls, new_data = self.parser.parse(u, html_content)
                    temp_set |= new_urls
                except BaseException as e:
                    print('craw failed, result %s ' % e)
            temp = temp_set - temp

        # self.outputer.output_html()
    @staticmethod
    def is_freemarker_error(url, content):
        if content.find('FreeMarker template error') != -1:
            print('发现freeMark异常, 链接是%s' % url)
        else:
            print('%s正常' % url)




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



# def

#
# for u in get_urls():
#     check_freemarker_error(u, get_url_content(u))

if __name__ == '__main__':
    with open('data.json', 'r', encoding='utf-8') as jsonFile:
        data = json.loads(jsonFile.read())
        at = AutoTest(data)
        at.freemarker_check()

input('')
