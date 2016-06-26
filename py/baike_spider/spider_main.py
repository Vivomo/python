from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url, size):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                html_count = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_count)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)
                print('craw %d : %s' % (count, new_url))

                if count == size:
                    break
                count += 1
            except BaseException as e:
                print('craw failed on %d result %s' % (count, e))

        self.outputer.output_html()


if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/view/21087.htm'
    size = 100
    obj_spider = SpiderMain()
    obj_spider.craw(root_url, size)
