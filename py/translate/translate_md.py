import re
import os
import http.client
import hashlib
import urllib.parse
import random
import json
from py.utils import IO_util

"""
一个翻译makerdown的小程序
主要应用于翻译GitHub上那些没有翻译的文档
本程序相对于浏览器的全文翻译 优点在于 会避开一些专有名词(如React, Vue等)的强制翻译
"""

mdReg1 = re.compile('\[.+?\]\s*\(.+?\)')


class Translator(object):

    needless = [mdReg1]
    placeholder = '♏'

    def __init__(self, cfg):
        self.config = cfg
        with open(cfg['filePath'], 'r', encoding='utf-8') as file:
            self.task = map(self.parse, file.readlines())

    def translate(self):
        translate_content = map(lambda obj: obj['result'], self.task)
        print('\n'.join(translate_content))

    def parse(self, line):
        _line = line.strip()
        needless_str = []
        for reg in self.needless:
            needless_str += re.findall(reg, _line)
            _line = re.sub(reg, self.placeholder, _line)
        return {
            'raw': line,
            'result': _line,
            'needless': needless_str
        }

config = {
    'filePath': r'../../src/d3-api.md',
    'ignoreWords': ['React']
}

tl = Translator(config)
tl.translate()


