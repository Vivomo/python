from urllib.request import Request, urlopen
import http.client


class HtmlDownloader(object):

    def __init__(self):
        self.cookie_str = ''

    def download(self, url, decode=''):

        # if not url:
        #     return None
        # if not url.startswith('http://'):
        #     url += 'http://'
        req = Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:36.0) Gecko/20100101 Firefox/36.0')
        req.add_header('Cookie', self.cookie_str)
        response = urlopen(req)

        if response.getcode() != 200:
            return None

        try:
            read = response.read()
        except http.client.IncompleteRead as icread:
            read = icread.partial

        if decode:
            return read.decode(decode)
        else:
            return read

    def ping_success(self, url):
        return urlopen(url).getcode() == 200
