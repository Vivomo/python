from urllib import request
import http.client


class HtmlDownloader(object):
    @staticmethod
    def download(url, decode=''):

        if not url:
            return None
        if not url.startswith('http://'):
            url += 'http://'
        response = request.urlopen(url)

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
        return request.urlopen(url).getcode() == 200
