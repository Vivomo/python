import os


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        total_count = len(self.datas)
        freemarker_error_data = list(filter(lambda d: 'error' in d, self.datas))
        with open('output.html', 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<head><meta charset="utf-8"></head>')
            fout.write('<body>')
            fout.write('<h1>自动化测试结果</h1>')

            fout.write('<dl>')
            fout.write('<dt>链接访问总数</dt>')
            fout.write('<dd>%d</dd>' % total_count)
            fout.write('</dl>')

            fout.write('<dl style="color:red">')
            fout.write('<dt>错误链接数</dt>')
            fout.write('<dd>%d</dd>' % len(freemarker_error_data))
            fout.write('</dl>')

            fout.write('<ol>')
            for data in freemarker_error_data:
                fout.write('<li><span style="color:red;">%s</span>\t\t <a href="%s" target="_blank">%s</a></li>' %
                           (data['error'], data['url'], data['url']))
            fout.write('</ol>')

            fout.write('</body>')
            fout.write('</html>')

        os.startfile('output.html')
