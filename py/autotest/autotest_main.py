import http.client
import http.cookiejar
import json
from urllib import request
from py.autotest import url_manager


class AutoTest(object):

    def __init__(self, config):
        self.config = config
        self.urls = url_manager.UrlManager(config)
        pass

    def run(self):
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
        mainData = data['']
    print(root_url)

input('')
