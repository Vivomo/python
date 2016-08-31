class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        with open('output.html', 'w', encoding='utf-8') as fout:
            fout.write('<html>')
            fout.write('<head><meta charset="utf-8"></head>')
            fout.write('<body>')
            fout.write('<table width="100%" border="1" borderColor="#ccc">')

            fout.write('<tr>')
            fout.write('<td width="10%">序列</td>')
            fout.write('<td width="20%">标题</td>')
            fout.write('<td width="70%">简介</td>')
            fout.write('</tr>')

            for index, data in enumerate(self.datas):

                fout.write('<tr>')
                fout.write('<td>%d</td>' % (index+1))
                fout.write('<td><a href="%s" target="_blank">%s</a></td>' % (data['url'], data['title']))
                fout.write('<td>%s</td>' % data['summary'])
                fout.write('</tr>')

            fout.write('</table>')
            fout.write('</body>')
            fout.write('</html>')