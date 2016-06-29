import re

EnglishExp = re.compile(r'l_(\w+)\s*=\s*[\'\"](.+?)[\'\"]\s*<#--(.+?)-->')


class Line(object):

    EnglishExp = re.compile(r'l_(w+)')

    def __init__(self, line='', translate_result=None):
        self.line = line
        if translate_result:
            self.ch = translate_result['src']
            self.en = translate_result['dst']
            self.name = ('l_' + re.sub(r'\W', '', re.sub(r'\s+', '_', self.en.lower()))).strip()
        else:
            result = re.search(EnglishExp, line)
            if result:
                self.name = result.groups()[0]
                self.en = result.groups()[1]
                self.ch = result.groups()[2]
            else:
                self.en = ''
                self.name = ''
                self.ch = ''

    def __str__(self):
        return '\t[en:%s][ch:%s]' % (self.en, self.ch)

    def is_legal(self):
        return self.name != '' and self.en != '' and self.ch != ''

    def to_en(self):
        if self.is_legal():
            return '%s = "%s" <#--%s-->' % (self.name, self.en, self.ch)
        else:
            return self.line.replace('\n', '')

    def to_ch(self):
        if self.is_legal():
            return '%s = "%s"' % (self.name, self.ch)
        else:
            return self.line.replace('\n', '')
