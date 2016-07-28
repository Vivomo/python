import http.client
import http.cookiejar
from urllib import request


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
    if content.find('FreeMarker template error') != -1:
        print('发现freeMark异常, 链接是%s' % url)


for u in get_urls():
    check_freemarker_error(u, get_url_content(u))
